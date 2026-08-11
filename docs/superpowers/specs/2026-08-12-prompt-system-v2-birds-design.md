# Thiết kế Prompt System v2 và tái tạo visual plan cho video Birds

**Ngày:** 2026-08-12  
**Phạm vi:** Hệ thống tạo `Pormpt.md` của repository và hai bản ENG/VIE của video `Why Birds Don’t Get Electrocuted on Power Lines — Until They Do`  
**Trạng thái:** Đã được người dùng duyệt ở mức thiết kế hội thoại; chờ duyệt đặc tả thành văn trước khi lập kế hoạch triển khai

## 1. Mục tiêu

Thay pipeline “mỗi hàng timeline phải có một prompt video Gemini” bằng pipeline phân loại asset trước khi viết prompt:

```text
Evidence / narration
→ Scene Contract
→ Asset Router
→ Execution Spec
→ Preflight validation
→ Generate or build
→ Visual QA
→ Prompt refinement
```

Kết quả phải đồng thời đạt ba mục tiêu:

1. Chỉ giao cho generative video những cảnh model có thể thể hiện đáng tin cậy.
2. Biến prompt AI thành đầu ra được biên dịch từ một scene specification rõ ràng, thay vì dùng độ dài prompt để bù cho thiết kế yếu.
3. Tái tạo hai file Birds thành hướng dẫn sản xuất thực dụng, đồng bộ ngôn ngữ và không làm thay đổi voiceover đã khóa.

## 2. Quyết định kiến trúc

### 2.1. Schema sáu cột

`Pormpt.md` tiếp tục dùng đúng sáu cột nhưng đổi cột cuối:

| Timeline | Scene / Sequence | Asset | Nội dung chi tiết | Nguồn tham khảo | Execution Spec |
|---|---|---|---|---|---|

Mọi hàng phải có `Execution Spec`, nhưng chỉ hàng được Asset Router đưa sang generative video mới có prompt Gemini Omni/Veo copy-ready.

### 2.2. Các execution mode

Mỗi hàng khai báo đúng một mode chính:

- `REAL_SOURCE`: brief tìm footage thật, frame vào/ra, tiêu chí loại và giới hạn factual.
- `EDITOR_MG`: build spec cho typography, diagram, 2D/3D hoặc motion graphic cần độ chính xác.
- `GMO_TEXT_TO_VIDEO`: text-to-video khi model tự quyết định appearance và composition.
- `GMO_REFERENCE_VIDEO`: reference khóa subject/look; prompt chỉ định chuyển động và delta.
- `VEO_FIRST_FRAME`: frame đầu khóa trạng thái ban đầu.
- `VEO_FIRST_LAST`: hai frame khóa trạng thái đầu/cuối; prompt mô tả chuyển tiếp vật lý.
- `HYBRID`: base plate và lớp editor-controlled được tách rõ.

Không tạo prompt video để lấp đầy schema. `EDITOR_MG` không được compile thành Gemini/Veo prompt.

## 3. Scene Contract

Mỗi cảnh AI hoặc hybrid phải được thiết kế từ contract có các trường:

- `PURPOSE`
- `CLAIM_BOUNDARY`
- `REPRESENTATION`
- `INITIAL_STATE`
- `INVARIANTS`
- `DOMINANT_CHANGE`
- `FACTUAL_GUARDRAIL`
- `NOT_YET_TRUE`
- `FORBIDDEN_INFERENCE`
- `VISUAL_SEMANTICS`
- `END_STATE`
- `FAILURE_MODES`
- `GENERATION_MODE`

Contract được trình bày gọn trong `Execution Spec` của hàng tương ứng. Những trường không áp dụng cho `REAL_SOURCE` hoặc `EDITOR_MG` được thay bằng brief/build spec chuyên biệt, không điền hình thức.

### 3.1. Invariants

Invariants phải khóa những yếu tố model thường tự thay đổi:

- số lượng vật thể;
- identity và anatomy;
- hình học, topology và điểm tiếp xúc;
- môi trường, ánh sáng và screen direction;
- vùng ảnh do reference/frame sở hữu.

### 3.2. Temporal state

`NOT_YET_TRUE` xác định những trạng thái cơ chế chưa được phép xuất hiện. Trường này ngăn model gộp nhiều giai đoạn vật lý vào một clip hoặc tạo payoff quá sớm.

### 3.3. Visual semantics

Khái niệm vô hình như điện thế, dòng điện hoặc điện trường không được xuất hiện dưới dạng từ trừu tượng chưa định nghĩa. Contract phải mô tả representation bằng pixel, đồng thời chỉ ra các substitution bị cấm như sparks, neon strands, network nodes hoặc magic glow.

## 4. Asset Router

Router áp dụng theo thứ tự:

1. Nếu footage/evidence thật giúp người xem quan sát hiện tượng, chọn `REAL_SOURCE`.
2. Nếu cảnh cần label, phép đo, topology, phương trình hoặc quan hệ kỹ thuật chính xác, chọn `EDITOR_MG`.
3. Nếu cần natural action hoặc reconstruction không thể quay an toàn, cân nhắc AI video.
4. Nếu cảnh cần photoreal base và lớp kỹ thuật chính xác, chọn `HYBRID` rồi tách base plate khỏi overlay.
5. Nếu một clip chứa nhiều thay đổi độc lập, tách thành nhiều asset hoặc chuyển phần chính xác sang editor.

Router là gate bắt buộc trước Prompt Compiler.

## 5. Prompt Compiler

Prompt được biên dịch theo mode:

- Text-to-video: subject, initial state, một dominant change, environment, camera, allowed representation và exclusions.
- Reference video: reference sở hữu appearance/composition; prompt tập trung vào motion, timing và phần được phép thay đổi.
- First frame: prompt tiếp tục từ trạng thái của frame đầu, không mô tả lại hoặc mâu thuẫn với frame.
- First/last frame: hai frame sở hữu điểm đầu/cuối; prompt chỉ mô tả transition vật lý giữa chúng.
- Hybrid: prompt chỉ tạo base plate; build spec riêng điều khiển overlay.
- Technical graphic: không compile sang generative video.

Mỗi prompt AI có duration 4–10 giây, một dominant change và `TIMED ACTION` liên tục từ `0.0 s` đến đúng duration. Prompt dùng `ALLOWED REPRESENTATION` trước `EXCLUDE`; exclusion phải bám failure mode của cảnh, không dùng negative soup chung.

## 6. Thiết kế riêng cho video Birds

Router dự kiến:

| Asset | Mode | Quyết định |
|---|---|---|
| `REAL-01` | `REAL_SOURCE` | Giữ khu dân cư và đường dây thật để thiết lập hệ thống. |
| `AI-01` | `HYBRID` | Tạo base plate/transition có kiểm soát; đường trace hệ thống và các dấu hiệu kỹ thuật do editor dựng, không giao cho model như điện phát sáng. |
| `REAL-02` | `REAL_SOURCE` | Giữ đàn chim thật làm observation. |
| `AI-02` | `GMO_REFERENCE_VIDEO` hoặc `VEO_FIRST_FRAME` | Reference khóa chim, dây, nền trời và hướng tiếp cận; prompt chỉ điều khiển bay đến, đáp và ổn định. |
| `EDIT-01` | `EDITOR_MG` | Dùng output đã duyệt; không tạo asset mới. |
| `MG-01` | `EDITOR_MG` | Ba observation có typography do editor kiểm soát. |
| `AI-03` | `GMO_TEXT_TO_VIDEO` | Ẩn dụ có chủ ý, gắn rõ conceptual representation; khóa silhouette và dominant change. |
| `MG-02` | `EDITOR_MG` | Sơ đồ nhánh dòng điện do editor dựng chính xác. |
| `TEXT-01` | `EDITOR_MG` | Typography thuần editor. |
| `AI-04` | `VEO_FIRST_LAST` hoặc `HYBRID` | Khóa frame toàn thân và macro hai điểm tiếp xúc; mọi label/potential gradient do editor dựng. |
| `MG-03` | `EDITOR_MG` | `V₁`, `V₂`, bracket và `V₁ ≈ V₂` do editor kiểm soát. |
| `REAL-03` | `REAL_SOURCE` | Chuyển động cất cánh thật; không ngụ ý tai nạn. |
| `MG-04` | `EDITOR_MG` | Hai topology nguy hiểm được dựng thủ công, không tạo electrocution giả. |
| `TEXT-02` | `EDITOR_MG` | Payoff từ footage thật đã duyệt. |

Quyết định cuối giữa `GMO_REFERENCE_VIDEO`/`VEO_FIRST_FRAME` và `VEO_FIRST_LAST`/`HYBRID` sẽ được ghi dứt khoát trong kế hoạch triển khai sau khi kiểm tra feature/mode hiện hành từ tài liệu Google chính thức. Không thay đổi loại asset hoặc claim để phục vụ công cụ.

Hai bản ENG/VIE phải khớp timeline, Asset ID, mode, duration, state transition và exclusions. Bản ENG dùng prompt tiếng Anh; bản VIE dùng prompt tiếng Việt tự nhiên theo quy tắc hiện hành của `.agent/AGENT.md`.

## 7. Skill dự án và tài liệu điều phối

Tạo skill dự án `video-prompt-engineering` ở vị trí discoverable theo chuẩn Codex của repository. Skill gồm:

```text
video-prompt-engineering/
├── SKILL.md
├── references/
│   ├── asset-routing.md
│   ├── scene-contract.md
│   ├── generation-modes.md
│   ├── scientific-visual-semantics.md
│   ├── failure-modes.md
│   └── examples.md
├── scripts/
│   ├── lint_pormpt.py
│   └── validate_timeline.py
└── tests/
    ├── fixtures/good/
    └── fixtures/bad/
```

`.agent/AGENT.md` chỉ giữ các gate cấp dự án: phải load skill khi tạo/sửa `Pormpt.md`, chạy Asset Router và Scene Contract trước khi viết prompt, và không bắt mọi asset có prompt video.

Các tài liệu được cập nhật trong phạm vi liên quan:

- `docs/Bố_Cục_prompt.md`
- `docs/VISUAL STORYTELLING PLAYBOOK.md`
- `docs/Quy_trình.md`
- `docs/Check_List.md`

Không mở rộng sang thay đổi voice, research framework hoặc policy ngoài những tham chiếu cần đồng bộ schema.

## 8. Linter và regression suite

Linter tối thiểu kiểm tra:

- bảng có đúng sáu cột và timeline liên tục;
- mọi hàng có một execution mode hợp lệ;
- mode graphic không chứa prompt generative;
- mode AI có Scene Contract và prompt cần thiết;
- thuật ngữ trừu tượng nhạy cảm có `VISUAL_SEMANTICS`;
- cảnh cần continuity có `INVARIANTS`;
- mechanism có `FACTUAL_GUARDRAIL` và `NOT_YET_TRUE` khi áp dụng;
- timed action bắt đầu `0.0 s`, kết thúc đúng duration và không có gap/overlap;
- không dùng “scientifically grounded” thay cho physics constraint;
- ENG/VIE khớp Asset ID, timeline, mode và duration.

Regression fixtures mã hóa tối thiểu:

- `F001 MULTIPLE_ATTACHMENT`
- `F002 FIELD_TO_NETWORK`
- `F003 GEOMETRY_MORPH`
- `F004 ABSTRACT_OBJECT_SUBSTITUTION`
- `F005 TEMPORAL_STATE_COLLAPSE`
- `F006 PREMATURE_DISCHARGE`
- `F007 SCIENTIFIC_AMBIGUITY`

S07–S09 của project Lightning được dùng làm positive exemplars nếu nội dung thực tế của chúng vượt Scene Contract audit. Regression suite không tự đánh giá video; nó kiểm tra cấu trúc specification và các tín hiệu lỗi có thể phát hiện tĩnh.

## 9. Visual QA sau generation

Mỗi output AI được so với Scene Contract theo schema:

```text
PROMPT_ADHERENCE: PASS / FAIL
FACTUAL_GUARDRAIL: PASS / FAIL
INVARIANTS: PASS / FAIL
TEMPORAL_STATE: PASS / FAIL
FORBIDDEN_INFERENCE: PASS / FAIL
FAILURE_MODE: NONE / F00X
USABLE_RANGE: FULL / time range / NONE
ACTION: KEEP / TRIM / REGENERATE
```

Prompt đúng không đồng nghĩa output đúng. Chỉ output vượt QA mới được đề xuất dùng trong timeline.

## 10. Files trong phạm vi triển khai

- `.agent/AGENT.md`
- skill dự án `video-prompt-engineering/**`
- `docs/Bố_Cục_prompt.md`
- `docs/VISUAL STORYTELLING PLAYBOOK.md`
- `docs/Quy_trình.md`
- `docs/Check_List.md`
- `Video/Why Birds Don’t Get Electrocuted on Power Lines — Until They Do/eng/Pormpt.md`
- `Video/Why Birds Don’t Get Electrocuted on Power Lines — Until They Do/vie/Pormpt.md`

Hai file `Kich_Ban.md` không được sửa. Project Lightning chỉ cung cấp regression examples; việc tái tạo toàn bộ S01–S36 nằm ngoài phạm vi lần triển khai này.

## 11. Validation và tiêu chí nghiệm thu

1. Hash của hai file Birds `Kich_Ban.md` không đổi.
2. Hai `Pormpt.md` có đúng sáu cột và timeline liên tục `00:00–01:01`.
3. Mọi hàng có execution mode; chỉ route AI có prompt video.
4. Mọi route AI có Scene Contract đầy đủ, một dominant change và prompt theo mode.
5. Technical labels, topology và potential graphics không được giao cho generative video.
6. ENG/VIE đồng bộ về meaning, Asset ID, timecode, mode, duration và failure exclusions.
7. Linter pass với fixtures tốt và fail đúng failure class với fixtures xấu.
8. Không còn rule bắt mọi hàng phải có Gemini prompt trong các tài liệu điều phối đã sửa.
9. Không thêm dependency mới nếu standard library Python đủ dùng.
10. Git diff chỉ chứa các file trong phạm vi; không commit, branch hoặc push nếu người dùng không yêu cầu.

## 12. Rủi ro và giới hạn

- Static lint không chứng minh output video đúng vật lý; Visual QA vẫn cần người xem output thật.
- Tính năng Flow/Veo thay đổi theo model, tài khoản và khu vực; mode cụ thể phải được xác minh bằng tài liệu Google chính thức tại thời điểm triển khai.
- Một Execution Spec đầy đủ có thể dài; ưu tiên specification có cấu trúc và một dominant change, không tối ưu bằng cách nhồi thêm tính từ.
- Candidate footage và license vẫn cần kiểm tra trên trang asset gốc trước khi dùng; việc xuất hiện trong `Pormpt.md` không phải phê duyệt quyền.
