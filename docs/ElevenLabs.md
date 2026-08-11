---
title: "Quy trình ElevenLabs cho narration documentary tiếng Anh"
version: "1.2.0"
last_verified: "2026-08-11"
scope: "Voice selection, model, script preprocessing, pronunciation, pauses, QA và consent"
status: "Production guide"
---

# ELEVENLABS — QUY TRÌNH GIỌNG ĐỌC DOCUMENTARY

## 1. Mục tiêu

Tài liệu này chuẩn hóa narration tiếng Anh cho kênh curiosity documentary/video essay hướng đến khán giả quốc tế.

Giọng cần:

- General American rõ nhưng không cường điệu accent.
- Thông minh, tò mò, đáng tin và gần gũi.
- Nghe như một narrator đang khám phá câu chuyện cùng người xem.
- Có nhịp và contrast nhưng không giống quảng cáo, trailer hoặc bản tin giật gân.
- Ổn định qua nhiều episode.
- Đọc chính xác tên loài, hiện tượng, cơ quan khoa học, địa điểm, số liệu và đơn vị đo.

Nguồn sản phẩm chính thức: [ElevenLabs — Text to Speech](https://elevenlabs.io/docs/speech-synthesis/voice-settings).

## 2. Quy tắc quyền sử dụng và consent trước tiên

Chỉ sử dụng:

- Voice Library voice được tài khoản/gói hiện hành cho phép sử dụng.
- Voice Design do đội sản xuất tạo.
- Instant Voice Clone mà người dùng có quyền và consent hợp lệ.
- Professional Voice Clone do chính chủ tạo, xác minh và chia sẻ theo cơ chế chính thức.

Không:

- Clone người nổi tiếng, nhà báo, narrator hoặc người khác chỉ từ audio công khai.
- Giả mạo một người có thật hoặc làm họ nói điều họ chưa từng nói.
- Vượt qua voice verification.
- Dùng sample chưa rõ quyền sở hữu.
- Cho rằng “có thể chọn voice trong app” đồng nghĩa với sở hữu vĩnh viễn mọi quyền với voice đó.

ElevenLabs yêu cầu người tạo Instant Voice Clone xác nhận mình có quyền và consent: [Instant Voice Cloning](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning).

Professional Voice Clone chỉ được tạo từ chính giọng của người xác minh. Nếu một người muốn cho đội sản xuất dùng giọng, họ phải tự tạo/xác minh PVC rồi chia sẻ bằng cơ chế của ElevenLabs: [Professional Voice Cloning](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning).

Trước khi xuất bản nội dung kiếm tiền, lưu:

- Voice ID và tên voice.
- Loại voice: Library, Design, IVC hay PVC.
- Tài khoản/gói sử dụng.
- Terms/license version tại ngày tạo audio.
- Bằng chứng consent/release nếu có người thật.
- Ngày generate và project/episode sử dụng.

Điều khoản có thể thay đổi; kiểm tra [ElevenLabs Terms of Service](https://elevenlabs.io/terms-of-use) và [Voice Library Addendum](https://elevenlabs.io/vla) trước production thương mại.

## 3. Chọn model

| Nhu cầu | Model khởi điểm | Lý do | Rủi ro cần test |
|---|---|---|---|
| Narration dài, ổn định | Eleven Multilingual v2 | ElevenLabs mô tả là ổn định cho long-form | Ít điều khiển biểu cảm trực tiếp hơn v3 |
| Cold open hoặc đoạn cao trào | Eleven v3 | Biểu cảm, punctuation và audio tags mạnh | Biến thiên cao hơn; tag phụ thuộc voice |
| Preview nhanh, batch kiểm tra | Flash v2.5 | Nhanh và chi phí thấp hơn | Có thể kém nuance với số/thuật ngữ |
| Cân bằng latency/chất lượng | Turbo v2.5 | Dùng khi workflow cần tốc độ | Phải A/B với final-quality model |

Nguồn so sánh model: [ElevenLabs — Text to Speech models](https://elevenlabs.io/docs/speech-synthesis/voice-settings).

Khuyến nghị cho kênh:

1. Bắt đầu bằng **Multilingual v2** cho narration chính.
2. A/B một số đoạn bằng **Eleven v3**.
3. Chỉ chuyển toàn episode sang v3 khi voice đã qua consistency QA.
4. Không trộn model trong cùng một đoạn nếu timbre hoặc room tone khác rõ.

Tên model, giới hạn ký tự, tính năng và trạng thái preview có thể đổi. Kiểm tra lại trang model trước mỗi batch lớn.

## 4. Chọn voice

### 4.1. Voice brief

Voice mục tiêu:

- General American English.
- Adult, khoảng 30–45 tuổi.
- Trung tính vùng miền.
- Warm, grounded, quietly confident.
- Conversational documentary.
- Không “radio announcer”.
- Không “movie trailer”.
- Không breathy/ASMR.
- Không quá trẻ hoặc quá hoạt hình.

### 4.2. Prompt Voice Design

ElevenLabs khuyến nghị prompt gồm ngôn ngữ/biến thể, giới tính, tuổi, chất lượng, persona, emotion, timbre, pacing và delivery: [ElevenLabs — Voice Design](https://elevenlabs.io/docs/eleven-creative/voices/voice-design/).

~~~text
Native English, General American. Male, 35–45. Clean studio quality.
Persona: curious documentary narrator.
Emotion: grounded, warm, quietly confident.

Natural mid-low timbre with conversational intonation and restrained
emphasis. Clear consonants, relaxed but purposeful pacing, short reflective
pauses, and enough dynamic range to build curiosity without sounding
theatrical. Avoid a radio-announcer cadence, exaggerated movie-trailer
delivery, breathy ASMR, sales language, and a strong regional accent.
~~~

Biến thể nữ:

~~~text
Native English, General American. Female, 32–42. Clean studio quality.
Persona: intelligent documentary guide.
Emotion: thoughtful, composed, quietly curious.

Warm natural timbre, precise but conversational articulation, restrained
emphasis, and a steady pace that remains engaging during technical
explanations. Avoid news-anchor delivery, vocal fry, exaggerated enthusiasm,
breathy ASMR, and a strong regional accent.
~~~

### 4.3. Audition script

Không chọn voice chỉ bằng một câu ngắn. Dùng cùng một script 250–400 từ có:

- Cold open ngắn.
- Một đoạn giải thích kỹ thuật.
- Một con số lớn.
- Một acronym.
- Một địa danh Mỹ.
- Một câu tương phản.
- Một câu kết trầm.

Chấm từng voice:

| Tiêu chí | Điểm 1–5 |
|---|---:|
| General American tự nhiên | |
| Độ tin cậy | |
| Khả năng đọc số/đơn vị | |
| Nhịp câu ngắn và dài | |
| Không bị “AI announcer” | |
| Consistency giữa các take | |
| Phù hợp curiosity/mystery documentary | |

Giữ cùng text và settings khi A/B để tránh so sánh sai.

## 5. Settings: baseline để test, không phải công thức cố định

Các giá trị dưới đây là **heuristic baseline**. Chúng không đảm bảo kết quả và phải được A/B theo voice.

### 5.1. Multilingual v2 và model có settings tương đương

| Setting | Baseline thử nghiệm | Ý nghĩa thực hành |
|---|---:|---|
| Stability | 0.50 | Cân bằng biểu cảm và ổn định |
| Similarity | 0.75 | Bám voice tương đối chặt |
| Style exaggeration | 0.00 | Giảm artifact và biến thiên |
| Speed | 0.96–1.00 | Hơi chậm cho technical narration |
| Speaker Boost | A/B on/off | Khác biệt thường nhỏ; có thể tăng latency |

ElevenLabs cho biết mức thường dùng là stability khoảng 50, similarity khoảng 75 và khuyên giữ style ở 0 vì style exaggeration có thể làm output kém ổn định: [ElevenLabs — TTS product guide](https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech).

### 5.2. Eleven v3

Khởi điểm:

- Chọn **Natural** nếu giao diện cung cấp Creative/Natural/Robust.
- Dùng Creative chỉ cho đoạn cần biểu cảm mạnh và phải QA kỹ.
- Dùng Robust khi consistency quan trọng hơn audio tags.
- Không giả định Similarity hoặc Speaker Boost tồn tại trên v3; các setting này không được hỗ trợ trong hướng dẫn sản phẩm hiện hành.

Nguồn: [ElevenLabs — Prompting Eleven v3](https://elevenlabs.io/docs/best-practices/prompting) và [TTS product guide](https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech).

### 5.3. Target pace đo được

Đặt baseline **145–165 words per minute (WPM)** cho documentary tiếng Anh, sau đó A/B bằng retention và listening QA của chính kênh. Đây là heuristic sản xuất, không phải thông số chính thức của ElevenLabs hoặc công thức tăng retention.

- Đoạn giải thích nhiều số/thuật ngữ: thử khoảng 135–150 WPM.
- Đoạn kể chuyện hoặc transition đơn giản: có thể thử 155–170 WPM.
- Không tăng tốc để ép script dài vào target duration; cắt câu thừa trước.
- Đo WPM trên audio hoàn chỉnh có tính các pause có chủ đích: tổng số từ chia cho số phút narration.
- Ghi WPM thực tế vào mục voice note của `Kich_Ban.md`; không suy ra pace chỉ từ giá trị Speed.

### 5.4. Mặc định Kokoro và nguyên tắc runtime

- Với Kokoro, baseline đã được người dùng duyệt là `speed=0.86`.
- `0.86` là điểm xuất phát về trải nghiệm nghe, không phải công thức để đạt một WPM hoặc thời lượng cố định.
- Không hạ speed để kéo narration đến 8 phút hoặc mốc thời lượng khác.
- Không thêm câu, lặp ý hoặc viết dài hơn chỉ để giữ `speed=0.86` mà vẫn đạt một số phút định trước.
- Runtime thực tế được đo sau khi render. Timeline dựng được cập nhật theo audio đã duyệt.
- Chỉ thay đổi speed khi listening QA cho thấy giọng cụ thể quá nhanh hoặc quá chậm; ghi lý do và giá trị thực tế trong `Kich_Ban.md`.
- Chỉ mở rộng kịch bản khi thiếu story, evidence, mechanism, boundary hoặc payoff, không phải vì thiếu phút.

## 6. Script preprocessing

Text đưa vào ElevenLabs lấy từ cột **Lời thoại / Voiceover** của `Kich_Ban.md`. Cột này phải là bản clean đã chuẩn hóa để đọc; không tạo thêm một file TTS Markdown dễ lệch phiên bản.

### 6.1. Quy trình

1. Khóa factual script.
2. Khóa cột Voiceover làm bản TTS chuẩn; chỉ copy text này sang dịch vụ khi người dùng thực hiện bước bên ngoài.
3. Bỏ citation, URL, footnote và chỉ dẫn hình ảnh khỏi text đọc.
4. Chuyển số, ký hiệu, acronym và đơn vị thành cách đọc mong muốn.
5. Thêm punctuation, paragraph break và tag theo model.
6. Chia chunk theo ý nghĩa và scene.
7. Generate, nghe lại và cập nhật mục pronunciation/voice QA trong `Kich_Ban.md`.
8. Không sửa factual wording chỉ để che lỗi phát âm; nếu đổi cách đọc, cập nhật ngay cột Voiceover để chỉ còn một bản chuẩn.

ElevenLabs lưu ý số, ngày, tiền tệ, URL, địa chỉ, ký hiệu và abbreviation có thể bị đọc sai; nên chuẩn hóa thành dạng nói rõ ràng: [ElevenLabs — TTS best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices).

### 6.2. Quy tắc viết để nghe

- Mỗi câu ưu tiên một ý.
- Dùng active voice.
- Trộn nhịp short → medium → long → short.
- Dùng dấu chấm cho pause rõ.
- Dùng dấu phẩy để chia phrase, không nhồi quá nhiều mệnh đề.
- Tránh ngoặc đơn dài.
- Tránh slash, ampersand và ký hiệu không cần thiết.
- Không viết heading toàn chữ hoa trong text đưa vào TTS.
- Không dùng dấu ba chấm chỉ để kéo dài silence; nó thường mang sắc thái do dự.

## 7. Chuẩn hóa số, acronym và đơn vị

### 7.1. Ví dụ cho niche

| Script editorial | TTS render |
|---|---|
| 2.4 GW | two point four gigawatts |
| 345 kV | three hundred forty-five kilovolts |
| 99.9% | ninety-nine point nine percent |
| $12.5 billion | twelve point five billion dollars |
| 2024 | twenty twenty-four |
| I-95 | Interstate ninety-five |
| 3–5 years | three to five years |
| 1,200 MW | twelve hundred megawatts |
| 7:30 a.m. | seven thirty A.M. |
| 08/11/2026 | August eleventh, twenty twenty-six |

Chọn cách đọc số theo context, không áp dụng máy móc:

- “twenty twenty-four” phù hợp năm.
- “two thousand twenty-four” có thể phù hợp văn phong khác.
- “twelve hundred megawatts” thường tự nhiên hơn “one thousand two hundred megawatts”.
- Với audience quốc tế, ưu tiên metric; thêm đơn vị địa phương khi hữu ích: “ninety-seven kilometers — about sixty miles”.

### 7.2. Acronym

Lần đầu:

~~~text
The Federal Energy Regulatory Commission, or FERC...
~~~

Các lần sau, chốt một cách:

- Đọc từng chữ: F-E-R-C.
- Đọc như từ: chỉ khi cách đọc ngành thực sự phổ biến.
- Dùng pronunciation dictionary/alias thay vì hy vọng model tự đoán.

Không đổi cách đọc giữa các episode.

### 7.3. Mục pronunciation trong Kich_Ban.md

| Original | Spoken form | IPA/alias | Nguồn xác minh | Voice/model | Approved take | Ghi chú |
|---|---|---|---|---|---|---|
| PJM | P-J-M | alias | Official usage | Voice A / Mv2 | E03-C12-T2 | Spell out |
| ERCOT | ER-cot | alias/IPA | Official interview | Voice A / Mv2 | E03-C13-T1 | Stress first syllable |
| Appalachia | app-uh-LATCH-uh | IPA/alias | Dictionary + local source | Voice A / v3 | E05-C07-T3 | Regional variation |

Với v3, ElevenLabs hỗ trợ IPA đặt giữa dấu gạch chéo nhưng độ nhất quán không tuyệt đối. Với các model cũ, phoneme/alias support khác nhau; kiểm tra đúng model trước khi áp dụng: [ElevenLabs — Pronunciation best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices#pronunciation).

## 8. Pauses và emphasis theo model

### 8.1. Eleven v3

Eleven v3 **không hỗ trợ SSML break tags**. Dùng:

- Dấu chấm và paragraph break cho pause tự nhiên.
- Dấu ba chấm cho pause có sắc thái suy nghĩ/do dự.
- Viết hoa rất ít để tăng emphasis.
- Audio tags phù hợp với voice.

Ví dụ:

~~~text
[curious] The stones move across the desert.

But no one saw them move for decades.

Then, one winter morning, the first clue appeared:
a sheet of ice, thinner than a windowpane.

The answer was hiding in plain sight.
~~~

Tags như [curious], [whispers], [sighs] và các mô tả cảm xúc phụ thuộc mạnh vào voice. Không ép một neutral voice thực hiện delivery trái với character của nó. Nguồn: [ElevenLabs — Prompting Eleven v3](https://elevenlabs.io/docs/best-practices/prompting).

Quy tắc production:

- Tối đa một hoặc hai tag có mục đích trong một chunk.
- Không đặt tag ở mọi câu.
- Không dùng viết hoa cả cụm dài.
- Nếu cần silence chính xác, thêm silence trong NLE sau khi generate.

### 8.2. Model không phải v3 có hỗ trợ break

~~~text
AI needs power.
<break time="0.6s" />
A lot of it.
~~~

ElevenLabs cho biết break có thể đặt tối đa khoảng ba giây, nhưng dùng quá nhiều có thể gây tăng tốc, noise hoặc artifact: [ElevenLabs — How can I add pauses?](https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/how-can-i-add-pauses).

Baseline:

- 0.3–0.5 giây: chuyển phrase.
- 0.6–0.9 giây: contrast hoặc reveal.
- 1.0–1.5 giây: chapter beat hiếm.
- Trên 1.5 giây: ưu tiên dựng silence trong editor.

Các khoảng trên là heuristic dựng phim, không phải thông số chính thức của ElevenLabs.

## 9. Chunking và versioning

### 9.1. Chunk size

Baseline thực hành:

- Khoảng 250–800 ký tự cho một generation.
- Kết thúc ở ranh giới câu/đoạn/scene.
- Một chunk có một emotional intent.
- Không cắt giữa tên riêng, con số hoặc lập luận nhân quả.

Đây là heuristic. ElevenLabs lưu ý prompt v3 quá ngắn có thể thiếu ổn định, trong khi troubleshooting guide khuyên generation ngắn hơn khoảng 800–900 ký tự khi xử lý artifact: [Prompting v3](https://elevenlabs.io/docs/best-practices/prompting), [ElevenLabs troubleshooting](https://elevenlabs.io/docs/resources).

### 9.2. ID và take

Dùng tên:

~~~text
E03_COLDOPEN_C01_T01
E03_CH02_C07_T03
E03_OUTRO_C02_T02
~~~

Lưu kèm:

- Episode và chapter.
- Chunk text hash hoặc version.
- Voice ID.
- Model.
- Settings.
- Pronunciation dictionary version.
- Take được duyệt.
- Người duyệt và ngày duyệt.

Không ghi đè take đã duyệt. Nếu script đổi factual wording, tạo version mới.

## 10. QA giọng đọc

### 10.1. Content QA

- Mọi câu khớp factual script đã khóa.
- Không mất từ, lặp từ hoặc thêm filler.
- Số, phần trăm, tiền tệ và đơn vị đúng.
- Acronym và tên riêng khớp pronunciation ledger.
- Pause không làm đổi nghĩa.
- Emphasis đặt đúng factual contrast, không biến uncertainty thành certainty.

### 10.2. Performance QA

- General American không drift sang accent khác.
- Không announcer/trailer cadence.
- Không quá đều hoặc quá dramatic.
- Nhịp đủ chậm cho khái niệm kỹ thuật.
- Câu ngắn có lực nhưng không bị “robotic”.
- Timbre và khoảng cách microphone cảm nhận giống nhau giữa các chunk.

### 10.3. Artifact QA

- Không click, pop, metallic ringing hoặc breath lạ.
- Không tăng tốc cuối đoạn.
- Không có tiếng cười, thở dài hoặc noise ngoài ý muốn.
- Không pitch jump giữa hai take nối nhau.
- Không sibilance quá gắt.
- Không cắt mất phụ âm đầu/cuối.

Nếu lỗi:

1. Regenerate đúng chunk.
2. Giảm tag và punctuation phức tạp.
3. Tăng stability nhẹ hoặc chuyển Natural/Robust.
4. Đưa style exaggeration về 0.
5. Chia câu khó thành hai câu.
6. Chuẩn hóa pronunciation.
7. Thử voice khác nếu lỗi lặp lại.

### 10.4. Mix QA

- Xuất lossless nếu gói/workflow hỗ trợ.
- Normalize và xử lý loudness trong DAW/NLE, không cố sửa mọi vấn đề bằng TTS settings.
- Giữ room tone và EQ nhất quán giữa các chapter.
- Nghe bằng tai nghe, loa laptop và điện thoại.
- Kiểm tra narration trên nền music/SFX, không chỉ nghe solo.

## 11. Disclosure giọng AI

Theo ví dụ hiện hành của YouTube:

- Clone chính giọng của creator để làm voiceover/dub không mặc nhiên cần altered-content disclosure.
- Clone giọng của người khác để tạo voiceover/dub thuộc nhóm cần disclosure.
- Nội dung làm một người thật có vẻ đã nói điều họ không nói phải disclosure và có thể vi phạm thêm các chính sách khác.

Nguồn: [YouTube — Disclosing use of altered or synthetic content](https://support.google.com/youtube/answer/14328491).

Chính sách disclosure không thay thế consent, publicity rights, copyright, hợp đồng voice talent hoặc điều khoản ElevenLabs.

Thực hành an toàn:

- Không marketing giọng thiết kế như giọng của một người thật.
- Không đặt tên voice gây hiểu nhầm là celebrity hoặc public figure.
- Nếu narrator là một persona hư cấu, ghi rõ trong hồ sơ production.
- Nếu có voice talent, hợp đồng cần nêu rõ phạm vi clone, thời hạn, lãnh thổ, nền tảng, quyền thu hồi và cách xử lý model sau khi kết thúc.

## 12. Checklist xuất bản

- [ ] Voice/model/settings đúng episode bible.
- [ ] Cột Voiceover trong `Kich_Ban.md` đã khóa version.
- [ ] Mọi số, acronym, địa danh và tên riêng đã QA.
- [ ] Mục pronunciation trong `Kich_Ban.md` được cập nhật.
- [ ] Không có từ bị thêm, mất hoặc lặp.
- [ ] Accent, cadence và emotion nhất quán.
- [ ] Không có artifact.
- [ ] File mix đã nghe trên nhiều thiết bị.
- [ ] Quyền dùng voice và consent còn hiệu lực.
- [ ] Đã quyết định YouTube altered/synthetic disclosure.
- [ ] Đã lưu Voice ID, model, settings, take và ngày generate.

## 13. Các mục phải kiểm tra lại định kỳ

Kiểm tra hàng tháng hoặc trước mỗi season:

- [ ] Danh sách model TTS và model được khuyến nghị cho long-form.
- [ ] Trạng thái/khả năng của Eleven v3.
- [ ] Audio tags và SSML support theo từng model.
- [ ] Voice settings hiện có trên v3 và v2.x.
- [ ] Pronunciation dictionary, IPA và alias compatibility.
- [ ] Character limits và export formats của gói.
- [ ] Commercial-use terms của subscription.
- [ ] Voice Library terms và quyền của từng voice.
- [ ] IVC/PVC consent và verification rules.
- [ ] YouTube disclosure cho synthetic/cloned voice.

Nguồn kiểm tra:

- [ElevenLabs Text to Speech](https://elevenlabs.io/docs/speech-synthesis/voice-settings)
- [ElevenLabs TTS best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)
- [Prompting Eleven v3](https://elevenlabs.io/docs/best-practices/prompting)
- [Voice Design](https://elevenlabs.io/docs/eleven-creative/voices/voice-design/)
- [Voice Cloning overview](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning)
- [ElevenLabs Terms of Service](https://elevenlabs.io/terms-of-use)
- [YouTube altered/synthetic disclosure](https://support.google.com/youtube/answer/14328491)
