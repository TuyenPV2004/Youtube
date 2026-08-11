---
title: "Bố cục prompt hình ảnh photorealistic cho Google AI Pro / Flow"
version: "1.5.0"
last_verified: "2026-08-12"
scope: "Google Flow, Nano Banana, Ingredients/References, Veo và Gemini Omni"
status: "Production guide"
---

# BỐ CỤC PROMPT HÌNH ẢNH CHO GOOGLE AI PRO / FLOW

## 1. Mục tiêu

Tài liệu này dùng để tạo hình ảnh và cảnh minh họa AI cho kênh curiosity documentary/video essay tiếng Anh về:

- Hiện tượng tự nhiên và Extreme Earth.
- Động vật và cơ thể người.
- Vật lý đời thường.
- Những mystery trong thế giới thật có thể giải thích bằng khoa học.

Mục tiêu hình ảnh:

- Trông như ảnh documentary/editorial có thể được chụp bằng máy ảnh thật.
- Có logic vật lý, vật liệu, ánh sáng và tỷ lệ hợp lý.
- Giữ được continuity giữa nhiều cảnh.
- Hỗ trợ lời kể nhưng không thay thế tư liệu thật.
- Không khiến người xem nhầm hình AI là bằng chứng hoặc archival footage.

## 2. Quy tắc bất biến: AI không phải bằng chứng

> Hình AI chỉ được dùng để minh họa, tái dựng hoặc giải thích một ý đã được xác lập bằng nguồn độc lập.

Không được:

- Dùng hình AI để chứng minh một hiện tượng, loài vật, địa điểm, cấu trúc địa chất hoặc sự kiện có thật.
- Gọi hình AI là “archival footage”, “satellite image”, “security footage” hoặc “photo from the site”.
- Tạo chi tiết kỹ thuật bằng AI rồi dùng chính chi tiết đó làm factual claim.
- Dùng hình AI của một địa điểm cụ thể khi chưa có reference đáng tin cậy, rồi ngụ ý đó là địa điểm thật.
- Dùng hình AI thay cho bản đồ, sơ đồ kỹ thuật, hồ sơ quy hoạch hoặc ảnh hiện trường có nguồn.

Nếu hình ảnh mang tính chân thực, phải gắn tag phù hợp:

- **AI-GENERATED RECONSTRUCTION**
- **ILLUSTRATIVE VISUALIZATION**
- **CONCEPTUAL RENDERING — NOT AN ACTUAL FACILITY**

Chỉ dùng **ARCHIVAL FOOTAGE** cho tư liệu thật đã xác minh nguồn và quyền sử dụng.

YouTube yêu cầu khai báo nội dung altered/synthetic khi cảnh được tạo hoặc sửa đáng kể nhưng trông như thật, bao gồm cảnh chân thực không thực sự xảy ra. Khai báo đúng không tự động làm video mất khả năng kiếm tiền: [YouTube — Disclosing use of altered or synthetic content](https://support.google.com/youtube/answer/14328491).

## 3. Công cụ hiện hành và nguyên tắc Nano Banana-first

Flow hiện dùng các model thuộc họ Nano Banana để tạo/chỉnh sửa ảnh. Hộp prompt tiêu chuẩn cho phép chọn model, tỷ lệ khung hình, số kết quả và thêm Ingredients/References: [Google Flow Help — Create & edit images](https://support.google.com/flow/answer/16729550?hl=en).

Workflow phải là **Nano Banana-first**. Không xây pipeline mới phụ thuộc Imagen:

- Google đã đánh dấu Imagen là deprecated.
- Tài liệu Google ghi Imagen sẽ ngừng hoạt động ngày 17 tháng 8 năm 2026 và khuyến nghị chuyển sang Nano Banana: [Google AI Developers — Imagen deprecation](https://ai.google.dev/gemini-api/docs/imagen).
- Danh sách model và feature trong Flow có thể thay đổi theo gói, quốc gia và thời điểm: [Google Flow Help — Models & supported features](https://support.google.com/flow/answer/16352836?hl=en).

## 4. Quy trình từ evidence đến hình ảnh

### Bước 1 — Viết Visual Evidence Brief

Trước khi viết prompt, ghi:

| Trường | Nội dung cần có |
|---|---|
| Claim đang minh họa | Câu factual claim đã được kiểm chứng |
| Nguồn của claim | URL/tài liệu primary hoặc authoritative |
| Loại visual | Tư liệu thật, sơ đồ, bản đồ, AI reconstruction hay B-roll |
| AI được phép suy diễn gì | Mood, góc máy, nhân vật không định danh |
| AI không được suy diễn gì | Layout thật, logo, công suất, thiết bị, con số, sự kiện |
| Tag hiển thị | AI-GENERATED RECONSTRUCTION hoặc tag phù hợp |

### Bước 2 — Chọn vai trò của ảnh

Một ảnh chỉ nên có một nhiệm vụ chính:

- Establishing: đặt bối cảnh.
- Mechanism: giải thích hệ thống vận hành.
- Scale: cho thấy quy mô.
- Human impact: nối hệ thống với con người.
- Transition: chuyển chương.
- Reconstruction: hình dung một tình huống không có tư liệu.

### Bước 3 — Tạo reference trước khi tạo nhiều cảnh

Nếu có nhân vật, thiết bị hoặc địa điểm lặp lại:

1. Tạo hoặc chuẩn bị reference sạch.
2. Đặt tên riêng cho từng reference.
3. Chốt identity/wardrobe/material/palette.
4. Chỉ sau đó mới tạo shot list.

Google khuyến nghị Ingredients có nền sạch hoặc được tách nền, prompt không mâu thuẫn với reference và các reference có look-and-feel nhất quán: [Google Flow Help — Create videos and use Ingredients](https://support.google.com/flow/answer/16353334?hl=en).

## 5. Công thức prompt ảnh photorealistic

Cấu trúc gốc của Google cho ảnh chân thực là: loại shot + chủ thể + bối cảnh + ánh sáng + góc máy + lens. Mẫu chính thức: [Google AI Developers — Photorealistic image prompting](https://ai.google.dev/gemini-api/docs/image-generation#prompts-for-generating-images).

Dùng template mở rộng dưới đây. Trong `eng/Pormpt.md`, prompt vận hành viết bằng tiếng Anh. Trong `vie/Pormpt.md`, prompt phải được dịch sang tiếng Việt tự nhiên, giữ đúng thuật ngữ camera/production và không làm lệch ý nghĩa hình ảnh.

~~~text
PURPOSE AND FORMAT
A photorealistic editorial documentary still for a YouTube video.
Widescreen 16:9. Leave [left/right] negative space for captions.

SUBJECT
[Who or what is shown: age range, appearance, clothing, object details].
[Fixed identity details that must remain unchanged across scenes].

ACTION
[One clear, physically plausible action].
[Exact interaction between hands, body, tools, and environment].

SETTING AND PERIOD
[Specific but non-misleading place type, time of day, weather, and era].
[Factually checked architecture, equipment, clothing, and infrastructure].

COMPOSITION
[Extreme close-up / close-up / medium / wide / establishing shot].
[Eye-level / low-angle / high-angle / overhead].
[Subject placement, foreground, midground, background, negative space].

CAMERA AND OPTICS
Shot on a [full-frame/documentary] camera with a [24mm/35mm/50mm/85mm/
macro/telephoto] lens.
[Shallow/deep] depth of field, [static/fast-shutter] appearance.
Natural perspective, realistic optical falloff, restrained lens effects.

LIGHTING
[Soft overcast daylight / window light / practical industrial light /
golden-hour sunlight].
One coherent light direction, realistic shadow softness, natural exposure,
preserved highlight detail.

MATERIALS AND MICRO-TEXTURE
[Weathered steel, oxidized bolts, faded paint, woven fabric, dust,
fingerprints, condensation, skin pores, flyaway hair].
Surfaces respond naturally to light; physically plausible reflections.

COLOR AND REALISM
Natural documentary color, restrained saturation, realistic dynamic range,
subtle sensor grain, slight real-world imperfections.
Unretouched skin and natural facial asymmetry.

CONTINUITY
Match the supplied reference for [character/object/location].
Keep [face, hairstyle, clothing, prop, palette] unchanged.

CONSTRAINTS
[Exact number of people/objects].
Factually plausible construction and anatomy.
Exclude visible brand names, captions, logos, and watermarks.
~~~

Không bắt buộc điền mọi dòng. Nếu prompt bị quá tải, giữ lại theo thứ tự:

1. Subject.
2. Action.
3. Context.
4. Composition.
5. Lighting.
6. Lens.
7. Constraints.

## 6. Chọn shot, lens và ánh sáng

Các lựa chọn dưới đây là baseline nhiếp ảnh, không phải cam kết rằng model sẽ mô phỏng chính xác một camera vật lý.

| Nhu cầu | Shot/lens khởi điểm | Tác dụng |
|---|---|---|
| Quy mô data center, substation, cảng | Wide/establishing, 24–35mm | Thấy hệ thống và quan hệ không gian |
| Con người trong môi trường làm việc | Medium, 35–50mm | Tự nhiên, vẫn giữ được context |
| Chân dung narrator/worker | Medium close-up, 50–85mm | Ít méo mặt, tách nền vừa phải |
| Transformer, chip, connector, vật liệu | Close-up hoặc macro, 60–105mm | Nhấn cấu tạo và texture |
| Hành động xa hoặc wildlife | Telephoto | Nén phối cảnh, tách chủ thể |

Ánh sáng documentary nên có nguyên nhân rõ:

- Overcast daylight từ bầu trời.
- Sunlight từ một hướng.
- Practical light từ đèn công nghiệp.
- Window light từ cửa sổ thật trong cảnh.

Tránh yêu cầu đồng thời golden hour, fluorescent light, moonlight và studio rim light nếu không có lý do vật lý.

## 7. Ví dụ kỹ thuật về prompt composition

> Các ví dụ data center/power grid bên dưới chỉ minh họa cấu trúc prompt photorealistic và continuity từ phiên bản cũ; chúng không xác định niche hoặc lịch nội dung hiện tại. Khi sản xuất, thay subject bằng hiện tượng khoa học thật và áp dụng factual guardrail tương ứng.

### 7.1. Data center campus và power grid

~~~text
A photorealistic aerial editorial documentary photograph of a fictional but
physically plausible hyperscale data center campus in Northern Virginia,
shown as an illustrative reconstruction rather than a real named facility.
Four low rectangular server buildings sit beside a utility substation with
orderly transmission connections, service roads, stormwater ponds, and
modest perimeter landscaping. No company branding and no readable signs.

Wide establishing composition from a restrained oblique aerial angle,
captured with a 35mm-equivalent lens. The campus fills the middle ground;
the substation and transmission corridor remain clearly readable as part of
the same system. Soft early-morning overcast light, slight atmospheric haze,
natural shadows and neutral editorial color.

Concrete panels show subtle weathering, galvanized steel has realistic
variation, rooftops contain plausible mechanical equipment without
fantastical machinery. Realistic scale, roads, vehicles, fencing, cable
routing, reflections and vegetation. Widescreen 16:9 with clean negative
space in the upper left for a chapter title.

Constraints: conceptual facility only, not an actual site; coherent power
connections; no futuristic architecture, glowing servers, giant logos,
impossible transmission geometry, duplicated buildings, text, watermark,
excessive HDR, CGI sheen, or oversaturation.
~~~

Tag bắt buộc trong video:

**CONCEPTUAL RENDERING — NOT AN ACTUAL FACILITY**

### 7.2. Transformer inspection

~~~text
A photorealistic editorial documentary medium-wide shot of an adult utility
maintenance engineer inspecting the exterior of a large power transformer at
a fictional American substation. The engineer wears a plain white hard hat,
safety glasses, work gloves, a navy flame-resistant jacket, and correctly
fitted protective equipment. One gloved hand rests naturally near an
inspection panel while the other holds a tablet with no readable screen text.

Eye-level composition on a full-frame documentary camera with a 50mm lens at
f/4. The engineer and transformer fittings are sharply focused; the distant
fence and buswork fall gently out of focus. Cool overcast daylight from one
direction, realistic soft shadows, neutral exposure and restrained color.

Weathered painted steel, ceramic bushings, galvanized fasteners, dust,
condensation, woven fabric and natural skin texture are visible. Subtle sensor
grain and real-world wear; no beauty retouching. Widescreen 16:9.

Constraints: one adult only, physically plausible equipment spacing and hand
contact, consistent PPE, coherent shadows and reflections; no utility logo,
readable data, text, watermark, extra fingers, fused hands, warped equipment,
plastic skin, science-fiction components, or dramatic sparks.
~~~

Tag:

**AI-GENERATED RECONSTRUCTION**

### 7.3. Data center cooling close-up

Chỉ dùng nếu cấu tạo đã được kiểm tra bằng ảnh/tài liệu thật.

~~~text
A photorealistic macro editorial photograph of condensation forming on a
chilled-water pipe connection inside a fictional industrial cooling plant
serving a data center. The image focuses on the metal flange, insulated pipe,
fasteners, moisture droplets and a technician's gloved hand checking the
connection. The exact arrangement follows the supplied technical reference.

Macro lens, shallow but sufficient depth of field to keep the flange and hand
contact readable. Neutral industrial practical lighting, accurate metal and
rubber textures, restrained contrast, realistic moisture and reflections.
No readable labels, logos, alarms, leaks, sparks, or catastrophic damage.
Widescreen 16:9.
~~~

## 8. Ingredients, References và continuity

### 8.1. Reference pack tối thiểu

Mỗi subject lặp lại nên có:

- **CHARACTER_A_HEAD**: khuôn mặt ba phần tư, ánh sáng trung tính.
- **CHARACTER_A_FULL**: toàn thân, trang phục chuẩn, nền sạch.
- **PROP_A**: đạo cụ hoặc thiết bị riêng.
- **LOCATION_A**: không gian chuẩn nếu cần continuity địa điểm.

Không dùng reference:

- Có nhiều người thừa.
- Có logo hoặc text không muốn tái tạo.
- Có ánh sáng xung đột mạnh.
- Có góc nhìn làm che mất đặc điểm nhận dạng chính.
- Có chi tiết kỹ thuật chưa xác minh.

### 8.2. Continuity lock

Lưu một block bất biến và lặp nguyên văn:

~~~text
CONTINUITY LOCK — CHARACTER A
Adult male, approximately 42, oval face, short dark-brown hair with slight
gray at the temples, clean-shaven, medium build. Plain white hard hat with no
logo, navy flame-resistant work jacket, gray work trousers, black safety
boots. Keep facial structure, age, hair, body proportions, clothing colors
and PPE unchanged across every image.
~~~

Chỉ thay một biến mỗi lần:

- Action.
- Camera angle.
- Shot size.
- Lighting.
- Location.

Không thay nhiều biến cùng lúc nếu cần giữ consistency.

### 8.3. Quy trình nối cảnh

1. Chọn generation tốt nhất làm canonical reference.
2. Lưu frame đạt chuẩn vào project.
3. Dùng lại reference đó làm Ingredient hoặc start frame.
4. Nhắc rõ reference nào quyết định identity, object và location.
5. Nếu sửa, yêu cầu thay đúng một phần và giữ nguyên các phần còn lại.
6. So sánh với reference trước khi duyệt, không chỉ so với prompt.

Flow hỗ trợ dùng Ingredients để giữ nhân vật/vật thể và Frames để điều khiển điểm đầu/cuối; tính năng cụ thể phụ thuộc model hiện hành: [Google Flow Help — Create videos](https://support.google.com/flow/answer/16353334?hl=en).

## 9. Video AI: Gemini Omni / Veo

Trong `Pormpt.md`, **mỗi hàng timeline** phải có ít nhất một prompt video hoàn chỉnh và có thể copy trực tiếp, kể cả khi asset chính là footage thật hoặc graphic. Prompt tại các hàng đó là phương án bổ sung/thay thế hoặc motion reference; nó không đổi loại asset chính. Bản ENG dùng prompt tiếng Anh; bản VIE dùng prompt tiếng Việt đầy đủ, tự nhiên và không dùng chỉ dẫn kiểu “xem bản ENG”.

Hai bản phải giữ cùng Asset ID, duration, timecode, hành động, camera và negative constraints. Bản VIE không được giữ nguyên prompt tiếng Anh hoặc dịch từng chữ làm sai thuật ngữ sản xuất hình ảnh.

Trước khi viết prompt chi tiết, audit cả chuỗi theo năm trường: **chủ thể · hành động · quy mô · hình thức biểu đạt · thông tin mới**. Không duyệt hai prompt liền nhau chỉ vì câu chữ khác nếu output dự kiến vẫn là cùng một cảnh. Thay đổi lens, ánh sáng, thời tiết, màu hoặc camera movement không được tính là một visual idea mới.

Ví dụ cần tránh: ba prompt liên tiếp đều tạo `trời bão + tháp cao + sét`, dù một prompt dùng wide shot, một prompt dùng telephoto và một prompt đổi hình tia sét. Hướng đúng là chuyển chức năng và visual mode, ví dụ: **hiện tượng thật → thiết bị ghi nhận sự lặp lại → mô hình nhiều ứng viên trong điện trường**.

Cột cuối mang tên `Prompt Gemini Omni` và chỉ chứa prompt tạo video. Không đặt hướng dẫn cắt dựng, transition, overlay, compositing, typography hoặc color grading trong cột này.

Với Gemini Omni:

- Chọn duration linh hoạt **4–10 giây** theo lượng chuyển động cần thiết; **10 giây là giới hạn tối đa, không phải mặc định**.
- Nếu một hàng cần nhiều clip, viết nhiều prompt con có Asset ID riêng trong cùng ô; từng prompt con vẫn tuân thủ giới hạn 4–10 giây và có timed action độc lập.
- Một clip ưu tiên một hành động hoặc một biến đổi chính. Nếu beat cần nhiều thay đổi độc lập, tách thành nhiều asset hoặc để editor/đồ họa đảm nhiệm.
- Phần `TIMED ACTION` phải bắt đầu tại `0.0 s`, kết thúc đúng duration đã khai báo và phủ toàn bộ khoảng giữa bằng các đoạn thời gian liên tiếp.
- Mỗi đoạn thời gian nói rõ subject nào chuyển động, camera làm gì, chi tiết nào giữ nguyên và frame cuối chuẩn bị cho cảnh kế tiếp ra sao.
- Prompt phải nêu aspect ratio, phong cách documentary, continuity/reference, camera/look và negative constraints phù hợp riêng với shot.
- Không yêu cầu model sinh chữ, nhãn khoa học, số liệu hoặc sơ đồ kỹ thuật; các thành phần đó do editor dựng 2D/3D.

### Template Gemini Omni video

~~~text
Create one continuous [DURATION]-second, 16:9 [STYLE] shot of [SUBJECT] in [ENVIRONMENT].
[CONTINUITY OR REFERENCE LOCK].

TIMED ACTION
0.0–[A] s: [opening composition, subject state, camera state].
[A]–[B] s: [one visible action or controlled change].
[B]–[DURATION] s: [resolve the action and leave a clean exit frame].

CAMERA / LOOK: [shot size, lens/perspective, movement, light, color, realism].
NEGATIVE CONSTRAINTS: [shot-specific failures, unwanted objects, morphing, text, logos].
~~~

Với Veo, ảnh reference và prompt video có nhiệm vụ khác nhau:

- Ảnh reference khóa appearance và composition.
- Prompt video chủ yếu mô tả chuyển động, camera và thay đổi theo thời gian.

Công thức chính thức của Google cho Veo:

**Cinematography + Subject + Action + Context + Style & Ambiance**

Nguồn: [Google Cloud — Ultimate prompting guide for Veo](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1/) và [Google AI Developers — Veo prompt guide](https://ai.google.dev/gemini-api/docs/video).

### Template image-to-video

~~~text
[SHOT AND CAMERA]
[Shot size], [camera angle], [one camera movement].

[LOCKED SUBJECT]
Use the supplied reference for [named subject].
Keep face, clothing, proportions, colors, and key objects unchanged.

[ACTION]
The subject performs one clear action from beginning to end.

[ENVIRONMENT]
[Location, weather, time, background activity].

[MOTION AND PHYSICS]
Natural body mechanics, realistic weight and inertia, subtle secondary motion
in clothing/hair/environment, physically plausible shadows and reflections.

[LIGHT AND LOOK]
[Lighting], [color palette], photorealistic documentary style,
restrained motion blur and exposure.

[AUDIO]
Natural ambient sound only. No dialogue, narration, or music.

[CONSTRAINTS]
No scene change, no new people or objects, no camera morphing,
no identity or wardrobe change, no text or logos.
~~~

### Ví dụ

~~~text
Medium-wide eye-level shot. A very slow dolly in toward the utility engineer
from the supplied reference. He makes one small adjustment to the inspection
tool, pauses, and examines the transformer fitting. The equipment remains
structurally fixed; only his arms, jacket fabric and a light morning breeze
move. Cool overcast daylight, realistic soft shadows, restrained motion blur
and subtle handheld micro-movement. Natural industrial ambience only.
No dialogue, narration, music, new people, wardrobe change, camera orbit,
text, logo, sparks, smoke, equipment deformation, or identity drift.
~~~

Khi dùng Extend:

- Mô tả hành động tiếp tục từ frame cuối, không mở lại một câu chuyện mới.
- Giữ cùng hướng chuyển động, ánh sáng và nhịp camera.
- Không thêm nhân vật hoặc đạo cụ mới nếu không thật sự cần.
- Dùng clip ngắn và một hành động chính để giảm morphing.

Flow chỉ cho extend một số video do Veo tạo và giới hạn thay đổi theo model; kiểm tra trước mỗi đợt sản xuất: [Google Flow Help — Edit videos & build scenes](https://support.google.com/flow/answer/16935718?hl=en).

## 10. Constraints và negative prompt

### Trong prompt chính

Ưu tiên mô tả kết quả mong muốn:

- “single adult engineer” thay vì chỉ “no crowd”.
- “natural unretouched skin” thay vì chỉ “no plastic skin”.
- “coherent single-source daylight” thay vì “no bad shadows”.
- “conceptual facility with no company identity” nếu cần loại branding.

### Trong ô Negative Prompt riêng, nếu model/giao diện có hỗ trợ

Google khuyên liệt kê trực tiếp thành phần không muốn thấy, không viết câu lệnh dài kiểu “do not generate”: [Google AI Developers — Veo negative prompts](https://ai.google.dev/gemini-api/docs/video#negative-prompts).

~~~text
watermark, logo, captions, garbled text, duplicated people, extra limbs,
fused fingers, waxy skin, beauty retouching, warped architecture,
impossible reflections, floating objects, oversaturation, excessive HDR,
cartoon rendering, synthetic CGI appearance
~~~

Không dùng “negative prompt soup”. Chỉ liệt kê lỗi có khả năng xảy ra trong shot cụ thể.

## 11. Realism QA bắt buộc

### 11.1. Con người

- Đúng số người.
- Mắt nhìn đúng hướng; đồng tử, mí mắt và răng tự nhiên.
- Bàn tay đủ ngón, đúng điểm tiếp xúc với công cụ.
- PPE thống nhất và hợp lý với công việc.
- Da còn texture, không waxy hoặc beauty-retouched.
- Tuổi, tóc, khuôn mặt, cơ thể và trang phục khớp reference.

### 11.2. Vật lý và camera

- Bóng đổ cùng hướng với nguồn sáng.
- Phản chiếu đúng vật thể và môi trường.
- Tỷ lệ người, xe, cột điện, transformer và tòa nhà hợp lý.
- Không có vật nổi, xuyên nhau hoặc thay đổi hình dạng.
- Depth of field phù hợp lens và khoảng cách.
- Không có highlight cháy giả, HDR quá mức hoặc bokeh vô lý.

### 11.3. Kỹ thuật và factual safety

- Không có text/con số giả được dùng như dữ liệu.
- Thiết bị không bị lắp theo cấu trúc bất khả thi.
- Bản đồ, sơ đồ, topology và power flow phải lấy từ nguồn thật hoặc được dựng thủ công từ dữ liệu thật.
- Nếu không xác minh được chi tiết, giảm độ cụ thể hoặc chuyển sang conceptual visualization.
- Một subject-matter reviewer phải duyệt các shot cận cảnh thiết bị quan trọng.

### 11.4. Continuity video

- Không identity drift.
- Không đổi số lượng người/vật.
- Không đổi thời tiết hoặc thời gian trong cùng shot.
- Không sinh thêm text/logo.
- Không camera morphing, jump hoặc geometry melt.
- Frame cuối đủ sạch để nối cảnh hoặc Extend.

## 12. Provenance và disclosure

`Pormpt.md` chỉ giữ Asset ID, nguồn factual/reference và prompt dùng để tạo asset ngay tại hàng timeline tương ứng. Không chèn bảng provenance, trạng thái sản xuất, quyền hoặc release gate vào tài liệu này. Nếu project cần lưu provenance vận hành, lưu cùng metadata/media artifact ở cấp project mà không làm loãng bản hướng dẫn edit.

Metadata nên lưu cho asset AI gồm:

| Trường | Ví dụ |
|---|---|
| Asset ID | AI-DC-EXT-001 |
| Model/tool | Flow / Nano Banana |
| Prompt version | v03 |
| Reference IDs | REF-DC-01, REF-SUB-02 |
| Generation date | 2026-08-11 |
| Intended use | Chapter 2 establishing shot |
| Provenance tag | CONCEPTUAL RENDERING |
| Factual source | URL báo cáo/ảnh tham chiếu |
| QA reviewer | Tên/ngày |
| YouTube disclosure | Yes / Not required / Review |

Tag nên xuất hiện đủ lâu để đọc được và không bị che bởi subtitle.

Đối với cảnh về:

- Một địa điểm có thật.
- Một sự kiện có thật.
- Một cá nhân có thật.
- Hạ tầng quan trọng.
- Health, finance, election, conflict hoặc disaster.

phải review disclosure kỹ hơn. Không tạo cảnh khiến người xem tin rằng một sự cố, phát ngôn hoặc hành vi đã thực sự xảy ra.

## 13. Các mục phải kiểm tra lại định kỳ

Kiểm tra hàng tháng hoặc trước một batch lớn:

- [ ] Model ảnh mặc định và các model còn khả dụng trong Flow.
- [ ] Ingredients, Frames, Extend và giới hạn theo model/quốc gia.
- [ ] Imagen đã ngừng hay còn giai đoạn chuyển tiếp nào.
- [ ] Hướng dẫn prompt/negative prompt mới của Nano Banana và Veo.
- [ ] Chính sách YouTube về altered/synthetic content.
- [ ] Chính sách monetization về inauthentic và reused content.
- [ ] Điều khoản thương mại của gói Google AI đang sử dụng.
- [ ] Quyền của toàn bộ reference upload lên Flow.

Nguồn kiểm tra:

- [Google Flow Help](https://support.google.com/flow/?hl=en)
- [Google AI image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Nano Banana prompt guide](https://deepmind.google/models/gemini-image/prompt-guide/)
- [Veo video generation](https://ai.google.dev/gemini-api/docs/video)
- [YouTube altered/synthetic disclosure](https://support.google.com/youtube/answer/14328491)
- [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en)
