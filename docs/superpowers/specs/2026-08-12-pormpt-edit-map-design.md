# Thiết kế Pormpt.md thành timeline asset-prompt map

**Ngày:** 2026-08-12  
**Phạm vi:** Video `Why Lightning Strikes the Same Place Again and Again` và rule dùng lại cho các video sau  
**Quyết định đã duyệt:** Mỗi hàng timeline có prompt video AI bằng tiếng Anh; mỗi clip AI dài linh hoạt 4–10 giây và 10 giây là giới hạn trên, không phải mặc định.

## 1. Mục tiêu

`Pormpt.md` là bản đồ asset và prompt video bám sát `Kich_Ban.md`. Tại mỗi thời điểm, tài liệu phải cho biết:

- lời thoại đang truyền đạt ý gì;
- đây là Scene độc lập hay Sequence gồm nhiều shot;
- loại asset chính nào biểu đạt ý đó tốt nhất;
- người xem cần nhìn thấy chủ thể, hành động và chuyển biến gì;
- footage thật hoặc factual reference có thể lấy từ đâu;
- Gemini Omni phải tạo chính xác cảnh gì trong từng khoảng giây.

`Pormpt.md` không chứa hướng dẫn edit, hồ sơ gate/compliance hoặc bảng trạng thái sản xuất.

## 2. Cấu trúc bảng

Mỗi bản ENG/VIE dùng đúng sáu cột:

| Cột | Nội dung bắt buộc |
|---|---|
| Timeline | Bám radio edit đã duyệt và phủ liên tục toàn bộ video. |
| Scene / Sequence | Ghi `Scene` cho một đơn vị hình ảnh chính; ghi `Sequence` khi một ý cần nhiều shot hoặc nhiều asset. |
| Asset | Chọn `REAL A-ROLL`, `REAL B-ROLL`, `AI VIDEO`, `2D GRAPHIC`, `3D GRAPHIC`, `EDITORIAL TEXT` hoặc `COMPOSITE`. |
| Nội dung chi tiết | Mô tả ý Voiceover, điều người xem nhìn thấy, chủ thể/môi trường, hành động thị giác, bố cục và trạng thái hình ở đầu/cuối cảnh. |
| Nguồn tham khảo | Nhiều footage candidate, nguồn official/factual và từ khóa tìm thay thế khi phù hợp. |
| Prompt Gemini Omni | Prompt video AI hoàn chỉnh bằng tiếng Anh để copy trực tiếp. Không chứa hướng dẫn edit bằng tiếng Anh hoặc tiếng Việt. |

Không có cột `Trạng thái` hoặc `Status`.

## 3. Quy tắc timeline và asset

- Mốc gốc lấy từ radio edit 06:22 và các beat trong `Kich_Ban.md`.
- Điểm tách dựa trên thay đổi về ý tưởng, hành động, quy mô, evidence, cơ chế hoặc visual payoff; không tách máy móc theo số giây.
- Dùng footage thật cho hiện tượng, môi trường, vật thể hoặc hạ tầng có thật khi có asset phù hợp.
- Dùng AI video cho cảnh khó quay, reconstruction, atmosphere, transition plate hoặc phương án bổ sung/thay thế.
- Dùng 2D/3D cho cơ chế, không gian, comparison và chi tiết cần kiểm soát.
- Dùng composite khi footage thật hoặc AI cần kết hợp graphic để truyền đạt cơ chế.
- Asset column vẫn thể hiện lựa chọn sản xuất chính; việc có prompt AI trong mọi hàng không biến mọi asset thành `AI VIDEO`.

## 4. Mức chi tiết của cột Nội dung

Mỗi dòng phải nêu được:

1. Ý Voiceover hoặc câu chuyển đang được hỗ trợ.
2. Vai trò của cảnh: quan sát, giải thích, so sánh, chuyển ý, hệ quả hoặc payoff.
3. Chủ thể và môi trường cụ thể.
4. Hành động thị giác chính.
5. Bố cục/camera mà người xem cần thấy.
6. Trạng thái hình ảnh ở đầu và cuối cảnh.

Cột này mô tả output và ý nghĩa, không hướng dẫn thao tác dựng.

## 5. Nguồn tham khảo

- Mỗi nhóm footage thật có nhiều nguồn; mục tiêu tối thiểu ba ứng viên khi thực tế cho phép.
- Ưu tiên nguồn official/archive cho factual reference và nguồn stock phù hợp cho footage ứng viên.
- Ghi link trực tiếp, mô tả ngắn và từ khóa tìm thay thế.
- Link chỉ là candidate/reference, không đồng nghĩa đã xác minh quyền sử dụng.
- Không tạo section riêng về rights/release trong `Pormpt.md`.

## 6. Prompt video Gemini Omni cho mọi hàng

- Mỗi Scene/Sequence đều có prompt video AI riêng, kể cả khi asset chính là footage thật, graphic, composite hoặc editorial text.
- Với hàng REAL, footage thật vẫn là lựa chọn chính; prompt AI dùng làm phương án bổ sung/thay thế hoặc motion reference nếu footage không phù hợp.
- Với hàng đồ họa, prompt tạo plate, không gian hoặc chuyển động nền. Không yêu cầu model sinh chữ, nhãn khoa học, số liệu hoặc sơ đồ kỹ thuật chính xác.
- Không còn câu như “cắt theo flash”, “thêm overlay”, “match frame”, “hard cut”, “giảm saturation” hoặc bất kỳ thao tác editor nào trong cột cuối.

### 6.1. Duration

- Mỗi prompt tạo clip dài 4–10 giây.
- Chọn duration ngắn nhất đủ hoàn thành một hành động thị giác.
- 4–6 giây cho một hành động/transition đơn giản; 7–8 giây cho thiết lập và phát triển cảnh; 9–10 giây cho chuyển biến phức tạp hơn.
- 10 giây là trần, không phải duration mặc định.

### 6.2. Timed action

- Bắt đầu tại `0.0 s` và kết thúc đúng duration đã khai báo.
- Các khoảng thời gian liên tiếp phải phủ toàn bộ clip, không có khoảng trống hoặc chồng lấn.
- Mỗi khoảng nói rõ subject làm gì, camera thay đổi thế nào và chi tiết nào phải giữ ổn định.
- Phần cuối mô tả một clean final frame phù hợp với ý tiếp theo, nhưng không dùng ngôn ngữ hướng dẫn edit.

### 6.3. Thành phần prompt

Mỗi prompt gồm:

1. Asset ID, duration và tỷ lệ 16:9.
2. Subject, environment và thời điểm.
3. Timed action phủ toàn bộ duration.
4. Camera, lens behavior và composition.
5. Lighting, color, texture và mức realism.
6. Continuity về chủ thể, geometry và bố cục khi cần.
7. Negative constraints riêng cho cảnh.

### 6.4. Timeline dài hơn 10 giây

- Một ô có thể chứa hai hoặc nhiều prompt con.
- Mỗi prompt con có Asset ID riêng, duration 4–10 giây và timed action độc lập.
- Không cần cộng cứng duration prompt bằng narration vì hàng có thể phối hợp footage thật, graphic hoặc giữ frame; tuy nhiên tập prompt phải biểu đạt đủ toàn bộ ý của hàng.

## 7. Quan hệ giữa ENG và VIE

- Hai file dùng cùng timeline, Scene/Sequence, Asset, nguồn và cấu trúc prompt.
- Bản VIE giữ cột nội dung bằng tiếng Việt.
- Cột `Prompt Gemini Omni` của cả hai bản viết hoàn toàn bằng tiếng Anh.
- Prompt của cùng Scene/Sequence phải giống nhau về nội dung, duration và timed action.
- Không dùng “xem prompt trong bản ENG”.

## 8. Các phần phải loại bỏ

- Tên cột và nội dung `Hướng dẫn edit / Edit direction`.
- Cột `Trạng thái / Status`.
- Các section Motion graphic/factual guardrail, rights/release gate, final gate, Production và Public release.
- Mọi chỉ dẫn cắt dựng, transition, overlay, compositing hoặc color grading trong cột prompt.

## 9. File cần thay đổi

- `Video/Why Lightning Strikes the Same Place Again and Again/eng/Pormpt.md`
- `Video/Why Lightning Strikes the Same Place Again and Again/vie/Pormpt.md`
- `.agent/AGENT.md`
- `docs/VISUAL STORYTELLING PLAYBOOK.md`
- `docs/Bố_Cục_prompt.md`

Không sửa `Kich_Ban.md` hoặc nội dung Voiceover.

## 10. Tiêu chí nghiệm thu

- Timeline liên tục từ 00:00 đến 06:22 và có đúng sáu cột.
- Mọi beat Voiceover có Scene/Sequence tương ứng.
- Asset mix vẫn giữ footage thật, AI, 2D/3D và composite theo nội dung.
- Cột cuối của cả ENG/VIE tên `Prompt Gemini Omni` và chỉ chứa prompt tiếng Anh.
- Cả 36 hàng có ít nhất một prompt video AI.
- Mỗi prompt dài 4–10 giây; timed action phủ đầy duration.
- Hàng cần nhiều clip có prompt con với Asset ID riêng và mỗi prompt không vượt quá 10 giây.
- Bản VIE có prompt tiếng Anh tương ứng đầy đủ với ENG.
- Không còn hướng dẫn edit hoặc các section đã yêu cầu loại bỏ.
- Hash hai file `Kich_Ban.md` không thay đổi.
