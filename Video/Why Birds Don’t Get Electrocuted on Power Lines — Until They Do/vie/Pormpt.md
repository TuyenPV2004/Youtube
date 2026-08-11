# Pormpt — Bản sản xuất hình tiếng Việt

> Tên file cố ý giữ đúng quy ước người dùng yêu cầu là `Pormpt.md`. Các prompt Veo vẫn để bằng tiếng Anh để có thể copy trực tiếp vào Google Flow; phần mục đích, vị trí, nguồn và thao tác dựng được giải thích bằng tiếng Việt.

## Mục tiêu sản xuất

**Bản dựng:** Video test nội bộ 61 giây  
**Khung hình:** 16:9  
**Ngữ pháp hình:** VIDEO THẬT → AI MINH HỌA → VIDEO THẬT → AI CÓ HÀNH ĐỘNG → GRAPHIC BIÊN TẬP → AI ẨN DỤ → MOTION GRAPHIC → CHUYỂN ĐỘNG THẬT → SƠ ĐỒ CƠ CHẾ → TRỞ LẠI MỞ ĐẦU  
**Mục tiêu sửa lỗi:** Không lặp lại kiểu phần lớn clip chỉ có cùng một con chim đứng trên dây rồi camera tiến vào chân.  
**Gate hiện tại:** KẾ HOẠCH ĐÃ SẴN SÀNG · CHƯA LẤY ASSET BÊN NGOÀI · CHƯA ĐƯỢC PHÁT HÀNH CÔNG KHAI

## Quy ước loại asset

- **REAL FOOTAGE:** Quan sát thực tế; chỉ dùng đoạn ngắn từ nguồn có license rõ.
- **AI VIDEO — ILLUSTRATION:** Hành động hoặc ẩn dụ khó quay an toàn; không bao giờ là bằng chứng factual.
- **MOTION GRAPHIC:** Giải thích do người dựng tự làm trong CapCut; dùng cho chênh lệch điện thế và hình học tiếp xúc.
- **EDITORIAL TEXT:** Điều khiển nhịp, bác bỏ và payoff; không thêm factual claim mới.

## Bản đồ media chính

| Timeline cuối | Asset ID + loại | Hình xuất hiện và thời lượng dùng cuối | Prompt hoặc nguồn video thật chính xác | Chuyển cảnh vào → ra | Quyền / trạng thái |
|---|---|---|---|---|---|
| 00:00–00:04 | `REAL-01` · REAL FOOTAGE | Toàn cảnh khu dân cư, nhìn rõ dây phía trên; dùng đúng 4 giây. | [Pexels item 35111175 — Sunny Suburban Street with Power Lines](https://www.pexels.com/video/sunny-suburban-street-with-power-lines-35111175/), creator Miltan Monjib. | Fade từ đen trong 6 frame → căn sợi dây chéo mạnh nhất khớp frame đầu `AI-01`. | CANDIDATE · người dùng tự tải ở trang item gốc và giữ bằng chứng. |
| 00:04–00:08 | `AI-01` · AI VIDEO — ILLUSTRATION | Chuyển từ lưới điện sang khu dân cư; dùng giây 00–04 của output, bốn giây còn lại chỉ là buffer ổn định và không đưa vào video. | Prompt đầy đủ `AI-01` bên dưới; tạo 8 giây bằng Veo 3.1. | Match-cut theo vị trí sợi dây → kết thúc bằng một dây sạch trên nền trời để cắt sang chim thật. | USER TỰ TẠO · lần AI đầu tiên phải có nhãn trên màn hình. |
| 00:08–00:13 | `REAL-02` · REAL FOOTAGE | Đàn chim thật trên dây có chuyển động nhỏ; dùng đúng 5 giây. | [Pexels item 11382880 — Birds Sitting on Power Lines](https://www.pexels.com/video/birds-sitting-on-power-lines-11382880/), creator khanhhoangminh. | Dây graphic thành dây thật → J-cut tiếng cánh nhẹ sang `AI-02`. | CANDIDATE · cần trang gốc và bằng chứng license. |
| 00:13–00:18 | `AI-02` · AI VIDEO — ILLUSTRATION | Một chim bay đến, đáp và bắt đầu gập cánh; dùng khoảng giây 01–06 của output. | Prompt đầy đủ `AI-02`; tạo 8 giây bằng Veo 3.1. | Khớp màu trời và góc dây của `REAL-02` → kết thúc ở tư thế bình thản, ổn định. | USER TỰ TẠO · cảnh synthetic chân thực. |
| 00:18–00:21 | `EDIT-01` · EDITORIAL CUT | Dùng frame cuối `AI-02`: một crop thân/mắt chim rồi giữ ngắn; tổng 3 giây. | Không cần asset mới; dựng từ output `AI-02` đã duyệt. | Một hard cut trong cùng scene → cắt theo khoảng im lặng sang `MG-01`. | EDIT GỐC · chỉ duyệt sau QA giải phẫu AI. |
| 00:21–00:27 | `MG-01` · MOTION GRAPHIC | Ba quan sát nhanh: dây nguyên / chim bình thản / trời bình thường; `NO FLASH`, `NO SHOCK`, `NO VISIBLE REACTION`. | Công thức dựng bên dưới. | Ba hard cut khớp lời thoại → cụm cuối tan vào texture lông. | EDIT GỐC · không cần asset ngoài. |
| 00:27–00:33 | `AI-03` · AI VIDEO — ILLUSTRATION | Ẩn dụ lá chắn lông hình thành, nứt và tan; dùng khoảng giây 01–07 của output. | Prompt đầy đủ `AI-03`; tạo 8 giây bằng Veo 3.1. | Match texture từ frame chim trước → lông tan thành sợi dây của `MG-02`. | USER TỰ TẠO · minh họa rõ ràng, không phải evidence. |
| 00:33–00:40 | `MG-02` · MOTION GRAPHIC | Dòng điện tiếp tục trên dây; hiện nhánh chim mờ; đặt câu hỏi với lối nói “điện chọn dây”. | Công thức dựng bên dưới. | Hạt lông từ `AI-03` tụ thành đường thẳng → rút màu về gần đen. | EDIT GỐC · wording vật lý đã đối chiếu `C-02`. |
| 00:40–00:44 | `TEXT-01` · EDITORIAL TEXT | Nền gần đen, sợi dây mảnh, chữ giữa `NEITHER ANSWER IS COMPLETE.` | Làm trong CapCut; không dùng AI. | Nhạc hạ gần im lặng → sợi dây mảnh trở thành dây trong `AI-04`. | EDIT GỐC. |
| 00:44–00:49 | `AI-04` · AI VIDEO — ILLUSTRATION | Một chuyển động duy nhất, có lý do, từ toàn thân chim đến đoạn dây ngắn giữa hai chân; dùng khoảng giây 02–07. | Prompt đầy đủ `AI-04`; tạo 8 giây bằng Veo 3.1. | Push qua sợi dây editorial → kết thúc bằng macro plate khóa máy, sạch. | USER TỰ TẠO · minh họa khoa học, không phải phép đo. |
| 00:49–00:52 | `MG-03` · MOTION GRAPHIC | Thêm `V₁`, `V₂`, ngoặc khoảng cách ngắn và `V₁ ≈ V₂`; đúng 3 giây. | Công thức dựng bên dưới. | Overlay mọc trên plate `AI-04` → đường ngoặc chuyển thành hướng bay trong `REAL-03`. | EDIT GỐC · không nói điện thế bằng nhau tuyệt đối. |
| 00:52–00:56 | `REAL-03` · REAL FOOTAGE | Chim thật cất cánh; chọn khoảnh khắc cánh mở và hình học tiếp xúc thay đổi; dùng đúng 4 giây. | [Pexels item 35676293 — Flock of Birds on Power Lines in Cloudy Sky](https://www.pexels.com/video/flock-of-birds-on-power-lines-in-cloudy-sky-35676293/), creator Zak Mir. | Motion-match từ hướng ngoặc/cánh → freeze trước khi tạo cảm giác có chấn thương. | CANDIDATE · tuyệt đối không gọi đây là footage điện giật. |
| 00:56–00:59 | `MG-04` · MOTION GRAPHIC | Hai sơ đồ sạch: dây mang điện–dây mang điện, rồi dây mang điện–phần nối đất; tổng 3 giây. | Tự dựng từ claim `C-03`; không lấy sơ đồ cột điện stock. | Silhouette cánh thành silhouette sơ đồ → giữ một đường dây sang frame tiêu đề cuối. | EDIT GỐC · cần review kỹ thuật. |
| 00:59–01:01 | `TEXT-02` trên `REAL-03` · EDITORIAL TEXT | Freeze/làm chậm frame thật sạch nhất và hoàn tất `UNTIL THEY DO.` | Không cần asset mới. | Chữ xuất hiện cứng đúng từ “deadly” → cắt ngay sang im lặng/đen. | EDIT GỐC dùng `REAL-03` đã duyệt. |

## Bộ quy tắc continuity cho AI

- Model mục tiêu: **Google Flow / Veo 3.1**.
- Tạo mỗi shot **8 giây, 16:9**, sau đó chỉ lấy đúng khoảng dùng cuối ghi trong bảng.
- Màu documentary: ánh sáng ngày cool-neutral tiết chế, tương phản tự nhiên, không grade blockbuster cam/xanh.
- Chim an toàn: một chim sẻ nhỏ chung chung, lông nâu than và xám, chân/cánh đúng giải phẫu, không khẳng định loài cụ thể.
- Dây an toàn: một sợi dây liên tục, không logo; trong cảnh đậu an toàn không có dây thứ hai, cột, biến áp hoặc phần nối đất trong tầm với.
- Không tạo chữ đọc được, logo, tia lửa, hồ quang, chấn thương, khói, xác chim, dây bất khả thi hoặc người đứng gần điện sống.
- Dòng điện không nhìn thấy bằng mắt. Mọi highlight chỉ là overlay khoa học mang tính biên tập.
- Giữ frame đầu và cuối sạch để match-cut. Không camera morphing, identity drift hoặc vật thể bất ngờ.

## Prompt Veo 3.1 đầy đủ

### AI-01 — Từ khu dân cư thật sang hệ thống vô hình

**Vị trí dùng cuối:** 00:04–00:08; tạo 8 giây rồi cắt.  
**Mục đích:** Đổi quy mô và thiết lập hệ thống trước khi đưa chim vào.

```text
Create an 8-second, 16:9 editorial documentary transition that begins realistic
and becomes a clearly illustrative scientific visualization. No people.

TIMED ACTION
0.0-1.0 s — Begin on a quiet suburban street in neutral morning daylight. One
overhead power line crosses the upper third of the frame, matching a preceding real
shot. The camera begins a controlled lateral move.
1.0-2.3 s — Keep the physical street visible while a restrained semi-transparent
technical overlay traces the same line toward several ordinary homes. This is an
editorial overlay, not glowing electricity and not lightning.
2.3-3.3 s — A few windows illuminate one after another, suggesting a working
neighborhood grid without displaying data, numbers or text.
3.3-4.0 s — Tilt to a cloudy sky and arrive on one clean dark wire crossing from
lower left to upper right, with negative space for a match cut to real birds.
4.0-8.0 s — Hold that clean composition with only subtle natural cloud movement.
This is an unused stability buffer so the first four seconds can be cut cleanly.

CAMERA AND LOOK
Controlled documentary camera, 35 mm equivalent lens, natural perspective,
realistic wood, cable and building textures, restrained cool-neutral grade, no
dramatic storm, no commercial gloss.

FACTUAL GUARDRAIL
Electric current is not visible. The tracing line is an unmistakable editorial
visualization of system connection, not evidence of literal glowing energy.

NEGATIVE CONSTRAINTS
No sparks, arcs, lightning, floating cables, impossible pole connections, extra
wires appearing, readable text, fake numbers, logos, watermarks, people, vehicles
moving through camera, rapid drone movement, geometry melting or CGI neon energy.
```

### AI-02 — Bay đến, đáp và bình thản ổn định tư thế

**Vị trí dùng cuối:** 00:13–00:18; giữ thêm frame cuối sạch cho 00:18–00:21.  
**Mục đích:** Tạo hành động có chủ đích; đây là beat đáp xuống hoàn chỉnh duy nhất.

```text
Create one continuous 8-second, 16:9 photorealistic wildlife-documentary shot of
exactly one generic small charcoal-brown passerine landing on exactly one overhead
wire. Neutral overcast daylight and a clean cloudy sky. No pole or second wire is
within reach.

TIMED ACTION
0.0-2.0 s — The empty wire holds in a medium-wide telephoto composition. The bird
enters naturally from the upper left, approaching along the wire's direction.
2.0-4.0 s — The bird brakes with anatomically correct wings and tail, reaches both
feet toward two nearby points on the same uninterrupted wire and makes a soft landing.
4.0-6.0 s — Its body absorbs the motion; the wings fold smoothly and completely.
6.0-8.0 s — The bird remains calm, alert and balanced, making only a tiny natural
head movement. End on a stable frame with the whole bird visible.

CAMERA AND LOOK
Locked medium telephoto camera with only a subtle tracking correction, 100 mm
equivalent lens, natural feather detail and motion blur, restrained documentary
color. Do not zoom toward the feet.

FACTUAL GUARDRAIL
Both feet contact nearby points on one wire only. The shot demonstrates ordinary
perching, not immunity to electricity and not a real documented incident.

NEGATIVE CONSTRAINTS
No sparks, arcs, injury, shock reaction, second conductor, grounded hardware,
transformer, human, nest, logo, watermark, text, extra bird, extra wings, extra toes,
fused talons, changing plumage, sliding feet, wire bending unrealistically, camera
morphing or slow-motion spectacle.
```

### AI-03 — Phá vỡ ngộ nhận “bộ lông là lá chắn”

**Vị trí dùng cuối:** 00:27–00:33; tạo 8 giây rồi cắt.  
**Mục đích:** Làm câu trả lời sai dễ nhớ bằng hình nhưng không trình bày nó như sự thật.

```text
Create an 8-second, 16:9 stylized editorial scientific visualization. It must look
designed and metaphorical, not like archival wildlife footage.

TIMED ACTION
0.0-2.0 s — Begin on an extreme macro field of realistic dry feather barbs moving
gently in neutral studio light.
2.0-4.0 s — Pull back as the feather pattern curves into a thin translucent shell
around a simple, anatomically plausible bird silhouette. The silhouette is not on a
power pole and no accident is shown.
4.0-6.0 s — Fine fractures travel across the shell while the bird silhouette remains
unchanged. The effect communicates an incomplete idea, not physical breaking glass.
6.0-8.0 s — The shell dissolves into individual feather fibers that stream rightward
and settle into one thin dark horizontal line, leaving negative space for editor text.

LOOK
Elegant museum-exhibit motion design, dark slate background, cream-gray feather
texture, restrained depth and light, slow deliberate camera, no horror tone.

FACTUAL GUARDRAIL
This is a visual metaphor for the mistaken belief that feathers are perfect armor.
It does not claim feathers have no insulating value.

NEGATIVE CONSTRAINTS
No readable text, labels, logo, watermark, sparks, electricity, injury, screaming
bird, broken bones, glass shards, fantasy magic, oversaturated glow, extra limbs,
fused anatomy, chaotic particles or abrupt camera movement.
```

### AI-04 — Cảnh cận điểm tiếp xúc duy nhất và có lý do

**Vị trí dùng cuối:** 00:44–00:49; tạo 8 giây rồi cắt.  
**Mục đích:** Hé lộ khoảng cách ngắn giữa hai điểm tiếp xúc và bàn giao sang potential graphic do người dựng tự làm.

```text
Create an 8-second, 16:9 photorealistic editorial science shot of exactly one calm
generic small passerine perched on exactly one uninterrupted overhead conductor.
Both feet touch nearby points on that same wire. No other electrical component is
within reach.

TIMED ACTION
0.0-2.0 s — Begin with the whole bird in a stable medium profile against a soft,
neutral cloudy sky. The bird remains calm and nearly still.
2.0-4.0 s — Make one slow, physically smooth camera move along the wire toward the
two feet. Keep the bird identity, light direction and wire geometry unchanged.
4.0-6.0 s — Arrive at a clean macro composition showing both feet and the short wire
segment between them. Both contact points must remain visible in the same frame.
6.0-8.0 s — Lock the camera. Add only an extremely subtle editorial color gradient
along the metal wire, almost unchanged between the feet, then end on a clean stable
plate with space above the contacts for editor-added V1 and V2 labels.

CAMERA AND LOOK
Natural documentary macro, 85-100 mm equivalent behavior, sufficient depth of field
to keep both feet and the wire segment sharp, realistic feather, scale and metal
texture, restrained cool-neutral grade.

FACTUAL GUARDRAIL
The color gradient is an illustrative potential map, not measured data. Do not show
current visibly crossing the bird and do not claim exact equality of potential.

NEGATIVE CONSTRAINTS
No second wire, pole, grounded hardware, sparks, arcs, glowing body, injury, text,
numbers, logo, watermark, extra toes, merged feet, changing leg position, duplicated
wire, sliding talons, impossible depth of field, camera jump, geometry melt or dramatic
storm light.
```

## Công thức dựng trong CapCut

| ID | Cách dựng chính xác | Quy tắc chuyển cảnh | Guardrail factual |
|---|---|---|---|
| `MG-01` | Tạo ba nhát cắt 1,5–2 giây từ footage/frame an toàn đã duyệt. Chữ trắng condensed: `NO FLASH`, `NO SHOCK`, `NO VISIBLE REACTION`; mỗi cụm fade 6–8 frame. | Hard cut theo từng câu đọc; không dùng overlay tia lửa stock. | Điều không xảy ra chính là quan sát; không bịa một sự cố điện. |
| `MG-02` | Vẽ một đường kim loại ngang. Animate chấm trung tính chạy tiếp trên dây. Thêm một nhánh song song mảnh mang hình chim đơn giản, để rất mờ. Chữ editor: `PATH OF LEAST RESISTANCE?`, có dấu hỏi. | Hạt lông `AI-03` tụ thành đường; rút màu trước `TEXT-01`. | Không nói điện “chỉ chọn một đường”. Số hạt không đại diện định lượng. |
| `MG-03` | Trên plate khóa của `AI-04`, đặt `V₁`, `V₂` ngay trên hai điểm chạm, ngoặc ngắn phía dưới, sau đó hiện `V₁ ≈ V₂`. | Dựng label tuần tự trong dưới 3 giây; ngoặc quét theo hướng cánh cảnh kế. | Dùng gần bằng; không bịa số volt. |
| `MG-04` | Panel A: hai dây mang điện có điện thế khác nhau được nối bởi silhouette chim. Panel B: một dây mang điện nối qua silhouette đến phần kim loại có ký hiệu ground. Mỗi panel khoảng 1,5 giây. | Motion-match cánh mở từ `REAL-03`; giữ lại một đường cho frame tiêu đề cuối. | Chỉ là sơ đồ; không lửa, không hoạt họa dòng qua nội tạng, không chấn thương, không khẳng định mọi cột điện đều giống nhau. |
| `TEXT-01` | Nền slate gần đen, một dây mảnh, chữ giữa `NEITHER ANSWER IS COMPLETE.` | Hạ nhạc ngay frame đầu; chữ vào hai nhịp: `NEITHER ANSWER`, rồi `IS COMPLETE.` | Chỉ là bước ngoặt biên tập. |
| `TEXT-02` | Freeze/làm chậm cuối `REAL-03`; chữ `UNTIL THEY DO.` vào đúng từ cuối. | Xuất hiện cứng, tối đa 2 giây, rồi đen. | Không ám chỉ clip nguồn thật ghi lại một vụ điện giật. |

## Brief chi tiết để người dùng tự tìm footage thật

Các link bên dưới chỉ là ứng viên, không bắt buộc phải dùng. Nếu xem clip và thấy không đúng brief, hãy tìm clip thay thế đáp ứng mô tả hình ảnh trước, sau đó mới kiểm tra license. Chỉ có title hoặc keyword liên quan là chưa đủ; frame thật phải đáp ứng yêu cầu.

### REAL-01 — Khu dân cư và hệ thống điện

- **Chức năng kể chuyện:** Thiết lập quy mô trước khi chim xuất hiện. Người xem phải hiểu ngay sợi dây thuộc về hệ thống điện của một khu dân cư bình thường, không phải một cảnh thiên nhiên tách biệt.
- **Bắt buộc nhìn thấy:** Một đường dân cư hoặc khu đô thị nhỏ yên tĩnh; nhiều ngôi nhà hoặc tòa nhà thấp; ít nhất một cột điện hoặc một tuyến dây phân phối phía trên có thể nhìn theo được. Dây phải nhìn rõ ngay từ giây đầu.
- **Hành động mong muốn:** Đời sống vẫn bình thường—cây lay nhẹ, xe ở xa hoặc đèn nhà sáng lên đều được—nhưng khung hình không được quá bận. Không có người nói thẳng vào camera.
- **Bố cục:** Ngang 16:9, tối thiểu 1080p. Toàn hoặc trung-toàn cảnh. Đặt sợi dây mạnh nhất ở 1/3 trên, lý tưởng là chạy chéo từ trái dưới lên phải trên để match với `AI-01`. Chừa nền trời sạch quanh dây.
- **Camera:** Tripod khóa máy, trượt ngang rất chậm hoặc pan có kiểm soát. Không drone nhanh, rung tay, zoom mạnh hay whip pan.
- **Ánh sáng và màu:** Buổi sáng, chiều muộn hoặc trời âm u mềm với màu trung tính. Màu documentary tự nhiên; tránh cảnh đêm neon, sét bão và grade cam/xanh kịch tính.
- **Thời lượng cần:** Clip nguồn có ít nhất 6 giây liên tục sạch. Bản dựng cuối dùng 4 giây tại `00:00–00:04`.
- **Frame vào tốt nhất:** Toàn cảnh ổn định để fade từ đen mà không gặp chuyển động lớn ngay lập tức.
- **Frame ra tốt nhất:** Dây điện tách rõ trên nền trời và có đường chéo sạch để match frame đầu `AI-01`.
- **Loại nếu:** Video dọc không crop sạch; dây quá nhỏ hoặc khó thấy; chỉ có tháp truyền tải cao thế mà không có khu dân cư; watermark, logo lớn, thông tin riêng tư đọc được, người thực hiện hành vi nguy hiểm, sét bão hoặc sự cố điện kịch tính.
- **Từ khóa tìm:** `suburban street overhead power lines 4k`, `residential neighborhood utility lines video`, `distribution power lines street documentary footage`, `quiet neighborhood electrical poles stock video`.

### REAL-02 — Nghịch lý bình thản

- **Chức năng kể chuyện:** Cho thấy hiện tượng thật trước khi giải thích: chim bình thản đứng trên dây và không có điều bất thường nào nhìn thấy được.
- **Bắt buộc nhìn thấy:** Ưu tiên 3–12 chim nhỏ thật đậu trên một dây utility nhìn rõ. Ít nhất một con phải quay đầu, nhảy, rung cánh, bay đến hoặc rời đi để cảnh không giống ảnh tĩnh.
- **Hành động mong muốn:** Chuyển động tự nhiên, cường độ thấp. Tương phản cần có là dây điện trông bình thường và hành vi chim hoàn toàn bình thường, không phải cảnh tượng ngoạn mục.
- **Bố cục:** Ngang 16:9, tối thiểu 1080p. Trung-toàn hoặc đủ rộng để thấy toàn thân chim và sợi dây. Giữ bầu trời thành negative space sạch. Không chọn macro chân hoặc frame bị một con chim đứng yên chiếm gần hết.
- **Camera:** Khóa máy hoặc pan cực chậm theo dây. Không lặp push-in vào chân, không rung tay và không telephoto shimmer quá nặng.
- **Ánh sáng và continuity:** Trời âm u mềm hoặc ánh sáng ngày trung tính, gần với bầu trời cuối `AI-01` và đầu `AI-02`. Tránh silhouette hoàng hôn trừ khi thiết kế lại toàn bộ shot liền kề cho khớp.
- **Thời lượng cần:** Ít nhất 7 giây sạch trong clip nguồn; bản cuối dùng 5 giây tại `00:08–00:13`.
- **Frame vào tốt nhất:** Góc dây và vị trí bầu trời gần khớp frame cuối `AI-01`.
- **Frame ra tốt nhất:** Một con bắt đầu cử động cánh nhỏ hoặc nhìn về hướng chim AI trong `AI-02` sẽ bay vào.
- **Giới hạn factual:** Chỉ dùng như B-roll chim thật trên dây nói chung. Không khẳng định chính sợi dây được quay đang mang điện nếu chủ nguồn không có tài liệu xác nhận.
- **Loại nếu:** Tất cả chim hoàn toàn bất động; clip chỉ zoom vào chân; chim đứng trên hàng rào, lồng hoặc cành cây; video cứu hộ/tai nạn; có chấn thương, logo, watermark, nén quá nặng, tia lửa giả hoặc license không rõ.
- **Từ khóa tìm:** `real birds perched on utility wire video`, `flock birds power line natural movement 4k`, `small birds on overhead wire documentary footage`, `birds landing leaving power line stock video`.

### REAL-03 — Hình học thay đổi khi cất cánh

- **Chức năng kể chuyện:** Tạo cầu nối bằng chuyển động thật từ trạng thái an toàn sang ngoại lệ. Cánh mở rộng làm câu “hình học thay đổi” trở nên hữu hình trước khi sơ đồ kỹ thuật xuất hiện.
- **Bắt buộc nhìn thấy:** Nhiều chim thật ban đầu còn đậu trên một dây nhìn rõ, sau đó một hoặc nhiều con cất cánh trong một hành động liên tục. Ít nhất một lần mở toàn cánh phải đọc được rõ trên nền trời.
- **Hành động mong muốn:** Đậu → khom/nghiêng người → mở cánh → chân rời dây. Ưu tiên một hành động sạch thay vì đàn chim đã bay hỗn loạn ngay từ đầu clip.
- **Bố cục:** Ngang 16:9, tối thiểu 1080p. Trung-toàn cảnh, nhìn được điểm bắt đầu tiếp xúc với dây và đủ trời cho cánh mở. Giữ dây trong khung suốt lúc cất cánh để editor có thể freeze quan hệ cuối.
- **Camera:** Khóa máy, tracking chậm hoặc slow motion tự nhiên có tiết chế. Chuyển động cánh phải đáng tin. Tránh speed ramp và crash zoom.
- **Ánh sáng và continuity:** Ánh sáng ngày trung tính hoặc trời âm u mềm, tương thích các cảnh chim trước. Background đủ đơn giản để chuyển thành sơ đồ silhouette trong `MG-04`.
- **Thời lượng cần:** Clip nguồn có 6–12 giây dùng được quanh lúc cất cánh. Bản cuối lấy 4 giây mạnh nhất tại `00:52–00:56`, cộng một freeze tùy chọn tại `00:59–01:01`.
- **Frame vào tốt nhất:** Chim vẫn còn chạm dây trong ít nhất vài frame trước khi bay.
- **Frame ra tốt nhất:** Silhouette cánh mở rõ, dây vẫn còn trong frame, thích hợp match-cut sang hai sơ đồ tiếp xúc.
- **Giới hạn factual:** Clip chỉ minh họa chuyển động và hình học tiếp xúc thay đổi. Tuyệt đối không mô tả hoặc dựng như thể đàn chim trong clip đã bị điện giật.
- **Loại nếu:** Clip bắt đầu sau khi chim đã rời dây; cánh bị nhà/cây che; có săn mồi, va chạm, hoảng loạn, chấn thương hoặc chim chết; extreme slow motion, video AI, watermark hoặc license không xác minh được.
- **Từ khóa tìm:** `birds taking off from power line slow motion`, `flock leaves overhead wire real footage`, `bird wings open takeoff utility wire 4k`, `birds perched then flying from wire documentary video`.

## Link ứng viên và quyền của video thật

Pexels hiện công bố ảnh/video của họ được tải và dùng miễn phí, được chỉnh sửa và được chia sẻ trên YouTube; attribution không bắt buộc nhưng được khuyến khích: [Pexels License](https://www.pexels.com/legal-pages/license/). Tuy vậy, tại thời điểm người dùng tải, vẫn phải lưu trạng thái trang item và điều khoản license. Có thể thay nguồn khác khi footage đáp ứng brief chi tiết phía trên và quyền sử dụng bằng hoặc rõ hơn.

| Asset | Trang item gốc | Creator hiển thị trên provider | Vị trí dùng cuối | Bằng chứng cần có trước khi APPROVED | Trạng thái hiện tại |
|---|---|---|---|---|---|
| `REAL-01` | [Pexels 35111175](https://www.pexels.com/video/sunny-suburban-street-with-power-lines-35111175/) | Miltan Monjib | 00:00–00:04 | File tải từ nguồn; ảnh/PDF trang item và Pexels License; ngày lấy; tên file local | HANDOFF TO USER · HOLD |
| `REAL-02` | [Pexels 11382880](https://www.pexels.com/video/birds-sitting-on-power-lines-11382880/) | khanhhoangminh | 00:08–00:13 | Như trên; xác nhận crop ngang và không có logo bên thứ ba; chỉ coi là B-roll chim-trên-dây chung, không phải bằng chứng sợi dây cụ thể này đang mang điện | HANDOFF TO USER · HOLD |
| `REAL-03` | [Pexels 35676293](https://www.pexels.com/video/flock-of-birds-on-power-lines-in-cloudy-sky-35676293/) | Zak Mir | 00:52–00:56 và frame freeze cuối | Như trên; xác nhận đoạn chọn có cất cánh và không bị gắn nhãn như một vụ tai nạn | HANDOFF TO USER · HOLD |

## Asset registry và gate phát hành

| Nhóm asset | Căn cứ provenance / quyền | Disclosure | Quyết định |
|---|---|---|---|
| `REAL-01` đến `REAL-03` | Trang item Pexels + Pexels License hiện tại; người dùng chưa tải file thật | Không gắn nhãn AI; credit creator là tùy chọn nhưng nên có | HOLD đến khi có file local và bằng chứng |
| `AI-01` đến `AI-04` | Người dùng tự tạo trong Google Flow / Veo 3.1 từ prompt trên; sau mỗi lần cần ghi tên output, ngày tạo và model | Quyết định upload an toàn nhất khi có cảnh synthetic chân thực: **Altered content = Yes**. Lần AI đầu gắn `ILLUSTRATIVE VISUALIZATION`. | HOLD; tạo và review từng cảnh trước khi dùng credit cho cảnh tiếp |
| `MG-01` đến `MG-04`, `TEXT-01`, `TEXT-02` | Tự dựng trong CapCut từ claim đã xác minh và frame nguồn đã duyệt | Không cần disclosure AI riêng nếu làm thủ công | APPROVED KHI ĐÃ TẠO VÀ KIỂM TRA |
| Narration Liam | Đã giữ tại `../Audio/SELECTED_AUDITION_Liam_Mv2_sp100_st50_sim75_style0.mp3`; chỉ dành cho test nội bộ; quyền release từ ElevenLabs đang tạm hoãn | Không làm người xem tin một người thật được nêu tên đang nói | GO CHO TEST NỘI BỘ · HOLD CHO PHÁT HÀNH |
| Music / SFX | Chưa chọn track ngoài | Nếu chưa có nguồn được duyệt, để video test không nhạc/SFX thay vì dùng asset không rõ quyền | HOLD / TÙY CHỌN |

## Quyết định với tám clip AI cũ

- Mặc định loại cả tám clip khỏi timeline đang hoạt động vì chúng lặp cùng thông tin hình ảnh.
- `Bird_landing_on_power_line_202608112057.mp4` chỉ được thay `AI-02` nếu thật sự có đủ bay đến → chạm dây → gập cánh và qua QA giải phẫu/continuity.
- Bảy clip còn lại là `REJECT` cho bản này, trừ khi review sau tìm thấy một hành động kể chuyện thực sự khác; chỉ zoom vào chân là không đủ.

## QA hình ảnh cuối

- [ ] Mỗi hàng thêm thông tin mới hoặc làm thay đổi cách hiểu của người xem.
- [ ] Không có hai hàng liên tiếp lặp cùng bố cục chim-trên-dây và cùng camera move.
- [ ] Mỗi clip thật đến từ đúng trang item và có bằng chứng quyền đã lưu.
- [ ] Prompt AI được tạo từng cảnh và review trước khi dùng credit cho cảnh kế.
- [ ] Không cảnh AI nào được trình bày như evidence hoặc footage điện giật thật.
- [ ] `V₁ ≈ V₂` và hai sơ đồ tiếp xúc nguy hiểm vẫn chính xác kỹ thuật.
- [ ] Cảnh AI chân thực đầu tiên có nhãn; disclosure upload được quyết định sau review bản cuối.
- [ ] Không có nhạc, SFX, voice hoặc stock chưa duyệt trong timeline phát hành.

**Bản test nội bộ:** GO sau khi người dùng cung cấp ba clip thật và các output AI đã duyệt.  
**Phát hành công khai:** HOLD.
