# QUY TẮC BẮT BUỘC CHO AI TRONG DỰ ÁN YOUTUBE

> Version: 2.1.0
> Last updated: 2026-08-11  
> Phạm vi: toàn bộ công việc nghiên cứu, viết kịch bản, tạo voice, tạo visual, dựng, xuất bản và phân tích video trong repository này.

Các quy tắc trong file này áp dụng cho mọi AI agent làm việc trong dự án. Nếu có xung đột, phải tuân theo system/developer/user instruction có mức ưu tiên cao hơn và thông báo rõ phần không thể áp dụng.

## 1. Bắt buộc đọc tài liệu trước khi làm việc

Trước khi đề xuất chủ đề, nghiên cứu, viết hoặc sửa kịch bản, tạo prompt, tạo giọng đọc, chọn tư liệu, dựng video hay tư vấn xuất bản, AI phải:

1. Liệt kê toàn bộ file Markdown trong thư mục **docs/**.
2. Đọc đầy đủ các tài liệu đó trước khi thực hiện công việc cho video đầu tiên trong phiên làm việc.
3. Đọc lại tài liệu chuyên trách liên quan ngay trước giai đoạn tương ứng.
4. Không tuyên bố đã đọc nếu file bị thiếu, không truy cập được hoặc nội dung bị cắt. Phải báo rõ file nào chưa đọc.
5. Khi tài liệu trong **docs/** có version mới, version mới nhất được ưu tiên.

Tối thiểu phải áp dụng:

- **docs/ĐỊNH HƯỚNG NỘI DUNG VÀ PHONG CÁCH SẢN XUẤT VIDEO.md** cho audience, định vị và content pillar.
- **docs/RESEARCH → EVIDENCE → SCRIPT → VISUAL RULE.md** cho research, source, evidence, claim và visual.
- **docs/PHONG CÁCH VIẾT VĂN CHO KỊCH BẢN DOCUMENTARY - VIDEO ESSAY.md** cho editorial voice và cấu trúc narration.
- **docs/Quy_trình.md** cho thứ tự sản xuất từ Discovery đến analytics.
- **docs/Check_List.md** cho gate kiểm tra và quyết định GO/HOLD/REJECT.
- **docs/Bố_Cục_prompt.md** cho Google Flow, Nano Banana, prompt, continuity và realism QA.
- **docs/VISUAL STORYTELLING PLAYBOOK.md** cho narrative beat, visual diversity, escalation, chuyển cảnh, phân công công cụ và prompt gate trước khi tạo media.
- **docs/ElevenLabs.md** cho voice rights, pronunciation, pacing, chunking và audio QA.
- **docs/Google.md** cho YouTube, YPP, copyright, Content ID, Community Guidelines, advertiser-friendly và AdSense.

Không được bỏ qua tài liệu chỉ vì AI đã đọc ở một cuộc trò chuyện trước nếu không thể xác nhận version hiện tại.

## 2. Mọi thông tin factual phải có căn cứ

Không được trình bày trí nhớ của AI, search snippet, nội dung do AI khác tạo hoặc suy đoán như sự thật.

Mọi claim factual, số liệu, trích dẫn, sự kiện lịch sử, nhận định về chính sách, tính năng sản phẩm hoặc thông tin có thể thay đổi phải:

1. Có nguồn phù hợp với chính claim đó.
2. Có URL trực tiếp đến tài liệu gốc khi nguồn có trên Internet.
3. Ghi publisher/author, title, publication date hoặc last updated nếu có.
4. Ghi data period đối với số liệu và forecast horizon đối với dự báo.
5. Ghi accessed date.
6. Ghi page, table, paragraph, docket hoặc timestamp khi có thể.
7. Phản ánh đúng phạm vi, định nghĩa, đơn vị và mức chắc chắn của nguồn.

Nếu không tìm được nguồn đủ tin cậy:

- ghi rõ **UNVERIFIED**;
- không đưa claim vào Clean VO hoặc title/thumbnail;
- không tự tạo số liệu, trích dẫn, URL hay tên nghiên cứu;
- đề xuất cách xác minh hoặc bỏ claim.

## 3. Thứ tự ưu tiên nguồn

Ưu tiên:

1. Luật, regulation, hồ sơ tòa án, hồ sơ cơ quan, dataset và tài liệu chính thức.
2. Nghiên cứu gốc, paper, methodology và dữ liệu của tổ chức chịu trách nhiệm thu thập.
3. Báo chí có quy trình biên tập, trade publication chuyên ngành và phân tích độc lập có phương pháp rõ.
4. Nguồn doanh nghiệp, investor material hoặc official statement chỉ dùng với nhãn self-interested và phải tìm đối chứng khi claim có tranh chấp.
5. Video YouTube, podcast, forum, comment và mạng xã hội chủ yếu dùng cho Discovery. Chúng chỉ được nâng thành primary evidence khi chính nội dung là bản ghi gốc có thể xác minh, như hearing, interview hoặc footage gốc.

Không đánh giá độ tin cậy chỉ theo website hoặc danh tiếng chung. Với từng nguồn phải xem:

- provenance: PRIMARY / SECONDARY / COMMENTARY;
- independence: INDEPENDENT / SELF-INTERESTED / MIXED;
- methodology: STRONG / ADEQUATE / WEAK / UNKNOWN;
- recency và claim fit.

## 4. Phân biệt fact với diễn giải

Mỗi claim phải có:

- **epistemic_type:** FACT / ESTIMATE / FORECAST / OPINION / INFERENCE;
- **narrative_role:** EVIDENCE / CONTEXT / COUNTERPOINT / UNCERTAINTY;
- **confidence:** HIGH / MEDIUM / LOW;
- source ID hoặc trạng thái UNVERIFIED.

Khuyến nghị sáng tạo, lựa chọn phong cách và quyết định biên tập không cần giả vờ là sự thật khách quan. Phải ghi rõ là:

- **EDITORIAL DECISION**;
- **WORKING HEURISTIC**; hoặc
- **INFERENCE**.

Không viết certainty mạnh hơn nguồn. Correlation không được gọi là causation nếu không có căn cứ phù hợp.

## 5. Không dùng AI làm nguồn

AI chỉ được dùng để:

- mở rộng keyword và query;
- tìm lead và counter-query;
- nhóm câu hỏi;
- tóm tắt tài liệu đã được cung cấp;
- kiểm tra tính nhất quán;
- phát hiện claim cần xác minh;
- hỗ trợ outline, draft và rewrite sau khi có evidence.

AI không phải citation. Mọi nguồn/URL do AI đề xuất phải được mở, đọc và xác nhận trước khi dùng.

## 6. Evidence, quyền tư liệu và hình AI là ba vấn đề khác nhau

- Nguồn đáng tin cậy về thông tin không tự tạo quyền sử dụng ảnh/video.
- Tư liệu công khai trên Google, YouTube, website chính phủ, archive hoặc mạng xã hội không mặc nhiên là public domain.
- Fair use không tự động phát sinh vì đã thêm voice-over, crop, zoom, color grade hoặc dùng clip ngắn.
- Mỗi asset phải có một hàng quyền sử dụng trong asset registry của **Pormpt.md** và trạng thái APPROVED trước khi vào timeline cuối.
- Asset PENDING, UNKNOWN hoặc BLOCKED không được dùng.
- Hình tạo bằng AI phải gắn **[VISUAL-AI]** và **[AI-NOT-EVIDENCE]**.
- Hình AI không được dùng làm bằng chứng cho người, địa điểm hoặc sự kiện có thật.
- Nội dung altered/synthetic có vẻ chân thực phải được đánh giá disclosure theo chính sách hiện hành trong **docs/Google.md**.

## 7. Mỗi video là một project riêng

Mọi video phải nằm trong một thư mục project riêng dưới:

**Video/<TITLE_VIDEO>/**

**<TITLE_VIDEO>** là title tiếng Anh hiện tại đã được người dùng chấp thuận hoặc working title đang được dùng chính thức cho project.

Không đặt file của video trực tiếp trong **Video/**. Không trộn research, script, voice, asset hoặc analytics của hai video khác nhau.

### 7.1. Quy tắc đặt tên thư mục

- Tên thư mục phải bám sát title video, dễ đọc và không dùng slug khó hiểu.
- Trên Windows, thay các ký tự không hợp lệ **< > : " / \ | ? \*** bằng dấu gạch ngang hoặc khoảng trắng phù hợp.
- Loại bỏ dấu chấm/khoảng trắng ở cuối tên.
- Không dùng tên thiết bị dành riêng như **CON**, **PRN**, **AUX**, **NUL**, **COM1** hoặc **LPT1**.
- Nếu title quá dài, rút gọn tên thư mục nhưng phải giữ đúng ý chính; title public đầy đủ vẫn được lưu trong **Kich_Ban.md**.
- Nếu đã có thư mục cùng tên, không ghi đè. Phải xác nhận đó có phải cùng project; nếu không, yêu cầu một tên phân biệt.
- Khi title thay đổi, cập nhật **Kich_Ban.md** trước. Chỉ đổi tên thư mục khi việc đổi tên không làm mất hoặc ghi đè dữ liệu.
- Trước mọi thao tác tạo, đổi tên hoặc di chuyển, phải xác nhận đường dẫn cuối vẫn nằm trong **Video/**.

### 7.2. Cấu trúc project mặc định

Mỗi project chỉ có **hai tài liệu Markdown chính cho mỗi ngôn ngữ**:

~~~text
Video/<TITLE_VIDEO>/
├── eng/
│   ├── Kich_Ban.md
│   └── Pormpt.md
└── vie/
    ├── Kich_Ban.md
    └── Pormpt.md
~~~

Giữ chính xác tên **Pormpt.md** theo quy ước của người dùng. Không tự đổi thành `Prompt.md`.

- **eng/** và **vie/** mỗi thư mục phải chứa đúng hai file `Kich_Ban.md` và `Pormpt.md`; không đặt thêm file hoặc thư mục con nào trong đó nếu người dùng chưa yêu cầu rõ.
- File media, project dựng, caption sau picture lock và bằng chứng quyền dạng ảnh/PDF/receipt phải nằm ở cấp project, bên ngoài **eng/** và **vie/**, ví dụ `Audio/`, `Video/`, `Edit/` hoặc `Rights_Proof/`; chúng phải được dẫn chiếu từ **Pormpt.md**.
- Research, checklist và log vẫn phải làm, nhưng được hợp nhất thành section/table trong hai tài liệu chính thay vì sinh file riêng.
- File cũ chỉ được archive hoặc xóa sau khi đã hợp nhất, kiểm tra đủ dữ liệu và có chỉ thị rõ của người dùng.

### 7.3. Nội dung bắt buộc của hai tài liệu

**Kich_Ban.md** là nguồn chuẩn duy nhất cho nội dung và voice, phải có:

- public title, project status, audience, central question, one-sentence promise và target duration;
- hướng đi chung theo từng cảnh/beat;
- bảng đúng 5 cột: **Thời lượng · Bố cục · Hình ảnh / B-Roll (Visual) · Lời thoại / Voiceover (Audio) · Âm thanh / Hiệu ứng (SFX/Notes)**;
- nguyên văn toàn bộ lời thoại trong cột Voiceover; không tạo một Clean VO độc lập có thể lệch phiên bản;
- bảng evidence/source gọn hợp nhất Source Table và Claim Ledger;
- pronunciation/voice note cần thiết và quyết định GO/HOLD/REJECT.

**Pormpt.md** là nguồn chuẩn duy nhất cho hình ảnh và sản xuất, phải có:

- master media map ghi timestamp, asset ID, loại **REAL / AI / MOTION GRAPHIC / DOCUMENT / EDITORIAL TEXT**, thời lượng dùng cuối và mục đích;
- vị trí chính xác của video AI và footage thật; link trực tiếp đến trang asset gốc đối với footage thật;
- với mỗi footage thật, ngoài link ứng viên phải có brief tự tìm chi tiết: chức năng kể chuyện; subject/environment bắt buộc; hành động mong muốn; bố cục; camera; ánh sáng/màu; độ phân giải/tỷ lệ; thời lượng nguồn và thời lượng dùng cuối; frame vào/ra; continuity với cảnh liền kề; giới hạn factual; tiêu chí loại; và từ khóa tìm kiếm;
- link footage chỉ là ứng viên. Nếu hình thật không đáp ứng brief thì phải thay, không được giữ chỉ vì title/keyword có vẻ đúng;
- prompt AI đầy đủ có timed action, continuity, factual guardrail, negative constraints và frame ra/vào;
- chuyển cảnh vào/ra cho từng beat;
- asset registry hợp nhất Rights Ledger, prompt/provenance log, cue sheet và production status;
- disclosure, visual QA và quyết định GO/HOLD/REJECT.

## 8. Đầu ra research bắt buộc trong từng project

Trước khi khóa lời thoại, **Kich_Ban.md** phải có bảng evidence/source bao gồm nguồn, provenance, freshness, claim, epistemic type, confidence, counterpoint và trạng thái. Đây là Source Table + Claim Ledger về mặt dữ liệu, không phải hai file riêng.

Trước khi khóa media map, **Pormpt.md** phải có asset registry bao gồm asset, owner, source URL, license, commercial/derivative rights, attribution, proof và trạng thái. Đây là Rights Ledger về mặt dữ liệu, không phải file riêng.

Trước khi tạo voice:

- **Kich_Ban.md** phải qua **docs/Check_List.md**;
- không còn blocker;
- cột Voiceover là bản clean để đọc, không chứa citation, visual tag hoặc editor note;
- mọi factual wording phải truy ngược được về bảng evidence/source trong cùng file.

Trước khi publish:

- asset registry trong **Pormpt.md** không còn asset chưa APPROVED trên timeline;
- mục final sign-off trong hai file là GO;
- title/thumbnail không overclaim;
- altered/synthetic disclosure đã được quyết định;
- Content ID/copyright checks đã được xử lý có căn cứ.

## 9. Cách trích dẫn trong câu trả lời và tài liệu

Khi trả lời người dùng về research hoặc policy:

- đặt link nguồn gần claim mà nó hỗ trợ;
- dùng tên nguồn mô tả rõ, không đưa bare URL nếu có thể;
- ưu tiên nguồn chính thức và primary;
- nêu ngày kiểm tra đối với thông tin có thể thay đổi;
- phân biệt điều nguồn nói trực tiếp với suy luận của AI.

Trong bảng evidence/source hoặc ghi chú của **Kich_Ban.md**, dùng tối thiểu:

~~~text
[CLAIM: C001]
[SOURCE: S001, page/table/timestamp]
[EPISTEMIC: FACT]
[ROLE: EVIDENCE]
[CONFIDENCE: HIGH]
~~~

Không đưa citation vào lời thoại clean trong cột Voiceover trừ khi narration chủ động gọi tên nguồn vì lý do biên tập.

## 10. Quy tắc dừng

AI phải dừng và báo người dùng thay vì tự suy đoán khi:

- chưa đọc được tài liệu bắt buộc trong **docs/**;
- title/project đích không xác định và có nguy cơ ghi vào nhầm thư mục;
- nguồn chính mâu thuẫn mà chưa thể giải quyết;
- claim quan trọng không xác minh được;
- quyền asset không rõ;
- thao tác có thể ghi đè hoặc làm mất project khác;
- cần mở rộng phạm vi, dùng tài khoản, gửi dữ liệu hoặc thực hiện hành động bên ngoài mà chưa được cho phép.

## 11. Kiểm tra trước khi hoàn thành công việc

Trước khi báo hoàn tất, AI phải xác nhận:

- [ ] Đã đọc đúng version tài liệu trong **docs/**.
- [ ] Mọi artifact nằm trong đúng **Video/<TITLE_VIDEO>/**.
- [ ] Mọi factual claim có nguồn hoặc được ghi UNVERIFIED và không đưa vào output cuối.
- [ ] Không có URL, số liệu hoặc trích dẫn do AI bịa.
- [ ] Fact, inference, forecast và opinion được phân biệt.
- [ ] Bảng evidence/source trong **Kich_Ban.md** và asset registry trong **Pormpt.md** được cập nhật khi có thay đổi.
- [ ] Không có asset chưa APPROVED trong đầu ra cuối.
- [ ] Kịch bản, voice, visual và policy checklist phù hợp các tài liệu chuyên trách.
- [ ] Đã báo rõ những phần chưa xác minh và rủi ro còn lại.
- [ ] Không tự thao tác tài khoản/dịch vụ bên ngoài; mọi bước bên ngoài đã được handoff và hướng dẫn trực tiếp cho người dùng.

## 12. Ranh giới thao tác trên dịch vụ bên ngoài

AI chỉ chuẩn bị, chỉnh sửa và kiểm tra hai tài liệu chính cùng các media/artifact nằm trong repository. Mọi thao tác có sử dụng tài khoản hoặc làm thay đổi trạng thái trên dịch vụ bên ngoài phải do người dùng tự thực hiện.

AI không được tự:

- điều khiển phiên trình duyệt hoặc ứng dụng đã đăng nhập của người dùng;
- thao tác trên ElevenLabs, Google Flow, YouTube Studio, thư viện stock, mạng xã hội hoặc dịch vụ bên thứ ba khác;
- sử dụng credit/quota, tạo media trên dịch vụ tính credit, chọn gói, nâng cấp, mua hàng hoặc thực hiện giao dịch;
- upload/download bằng tài khoản người dùng, gửi dữ liệu, thay đổi thiết lập tài khoản, publish, schedule, share hoặc xóa nội dung bên ngoài;
- tiếp tục một bước bên ngoài chỉ vì người dùng đã đăng nhập hoặc trước đó đã cấp quyền chung.

AI được phép nghiên cứu **read-only** trên các trang công khai để xác minh factual claim, chính sách và điều khoản khi quy trình yêu cầu. Việc này không được dùng phiên đăng nhập của người dùng, không được truyền dữ liệu riêng tư và không được gây side effect trên dịch vụ.

Khi quy trình đến một bước bắt buộc phải thực hiện bên ngoài, AI phải:

1. Hoàn thành trước mọi tài liệu và artifact nội bộ có thể chuẩn bị trong repository.
2. Ghi rõ trạng thái `HANDOFF TO USER` hoặc `HOLD`, lý do và điều kiện để qua gate.
3. Hướng dẫn trực tiếp trong cuộc trò chuyện **một bước tại một thời điểm**; không yêu cầu người dùng tự mở và tìm hướng dẫn trong file dự án.
4. Với mỗi bước, nêu chính xác nơi cần vào, thao tác cần làm, giá trị cần nhập/chọn, kết quả mong đợi và cảnh báo về credit, quyền hoặc giao dịch nếu có.
5. Chờ người dùng xác nhận đã hoàn thành bước hiện tại rồi mới hướng dẫn bước bên ngoài kế tiếp.
6. Chỉ cập nhật trạng thái PASS/APPROVED khi có bằng chứng phù hợp do người dùng cung cấp hoặc artifact kết quả đã được đưa vào project để kiểm tra.

Nếu người dùng muốn AI trực tiếp thực hiện một ngoại lệ trong tương lai, người dùng phải đưa ra chỉ thị mới, cụ thể cho đúng dịch vụ, đúng thao tác và đúng phạm vi. Không được suy rộng ngoại lệ đó sang bước khác hoặc dịch vụ khác.
