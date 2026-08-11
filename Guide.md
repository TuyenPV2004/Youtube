# Hướng dẫn tạo voice bằng Kokoro

Tài liệu này hướng dẫn tạo narration tiếng Anh từ cột **Lời thoại / Voiceover** trong `eng/Kich_Ban.md`.

## Quy tắc đã khóa

- Voice mặc định của series: `af_heart`.
- Kokoro mặc định: `speed=0.86`.
- Không giảm speed để kéo audio đến 8 phút hoặc một mốc thời lượng khác.
- Không thêm filler, lặp ý hoặc viết dài kịch bản chỉ để tăng runtime.
- Runtime là kết quả của lời thoại đã duyệt và nhịp nghe tự nhiên.

## 1. Mở PowerShell tại thư mục dự án

```powershell
Set-Location D:\Youtube
```

Các thành phần cần có:

```text
D:\Youtube\.venv-kokoro\
D:\Youtube\.tools\generate_kokoro_narration.py
Video\<TITLE_VIDEO>\eng\Kich_Ban.md
```

Script tự đọc các hàng timeline trong `Kich_Ban.md` và chỉ lấy nội dung của cột Voiceover. Citation, visual note và SFX không được đặt trong cột này.

## 2. Tạo voice cho video hiện tại

Chạy nguyên lệnh sau trong PowerShell:

```powershell
.\.venv-kokoro\Scripts\python.exe .\.tools\generate_kokoro_narration.py `
  "Video\Why Lightning Strikes the Same Place Again and Again\eng\Kich_Ban.md" `
  "Video\Why Lightning Strikes the Same Place Again and Again\Audio\Narration_af_heart_master.wav" `
  --voice af_heart `
  --section-pause 0.65
```

Không cần truyền `--speed`: công cụ đã dùng mặc định `0.86`.

Lệnh sẽ tạo hoặc ghi đè hai file:

```text
Video\Why Lightning Strikes the Same Place Again and Again\Audio\Narration_af_heart_master.wav
Video\Why Lightning Strikes the Same Place Again and Again\Audio\Narration_af_heart_master.json
```

- `.wav`: narration hoàn chỉnh, mono 24 kHz, PCM 24-bit.
- `.json`: manifest gồm voice, speed, runtime, WPM, hash lời thoại và timing từng đoạn.

## 3. Mẫu lệnh cho video khác

Thay giá trị `$title` bằng đúng tên thư mục video:

```powershell
$title = "TITLE_VIDEO"
$project = Join-Path "Video" $title
$script = Join-Path $project "eng\Kich_Ban.md"
$output = Join-Path $project "Audio\Narration_af_heart_master.wav"

.\.venv-kokoro\Scripts\python.exe .\.tools\generate_kokoro_narration.py `
  $script `
  $output `
  --voice af_heart `
  --section-pause 0.65
```

Ví dụ `$title`:

```powershell
$title = "Why Lightning Strikes the Same Place Again and Again"
```

## 4. Kiểm tra kết quả

Xem thông tin kỹ thuật của WAV:

```powershell
.\.venv-kokoro\Scripts\python.exe -c "import soundfile as sf; print(sf.info(r'Video\Why Lightning Strikes the Same Place Again and Again\Audio\Narration_af_heart_master.wav'))"
```

Xem manifest:

```powershell
Get-Content -Raw "Video\Why Lightning Strikes the Same Place Again and Again\Audio\Narration_af_heart_master.json"
```

Kiểm tra tối thiểu trong manifest:

- `voice` là `af_heart`.
- `speed` là `0.86`.
- `word_count` khớp kịch bản.
- `chunks` có đủ các đoạn timeline.
- `source_voiceover_sha256` thay đổi nếu và chỉ nếu nội dung Voiceover thay đổi.

Sau đó nghe toàn bộ WAV bằng tai nghe hoặc loa. Listening QA quan trọng hơn WPM hoặc tổng runtime.

## 5. Chỉ đổi speed khi listening QA yêu cầu

Nếu giọng thực sự quá nhanh hoặc quá chậm, có thể truyền speed khác:

```powershell
--speed 0.90
```

Chỉ thay đổi vì trải nghiệm nghe của voice cụ thể. Không dùng speed để ép video đạt một số phút.

## 6. Lỗi thường gặp

### `No timeline voiceover chunks found`

Kiểm tra bảng trong `eng/Kich_Ban.md`. Hàng thoại phải bắt đầu bằng timestamp, ví dụ:

```text
| 00:00–00:32 | ... |
```

### `Unexpected timeline row structure`

Một hàng timeline không còn đúng năm cột hoặc chứa ký tự `|` ngoài cấu trúc bảng. Sửa bảng trước khi chạy lại.

### Lỗi tải model từ Hugging Face

Lần chạy đầu tiên trên máy mới có thể cần Internet để tải `hexgrad/Kokoro-82M` và voice `af_heart`. Sau khi model đã được cache, các lần tạo sau có thể chạy cục bộ.

### File đầu ra đã tồn tại

Lệnh tạo voice sẽ ghi đè WAV và JSON cùng tên. Nếu cần giữ take cũ, đổi tên output trước khi chạy, ví dụ:

```powershell
"Video\TITLE_VIDEO\Audio\Narration_af_heart_take02.wav"
```

## 7. Sau khi tạo voice

1. Nghe toàn bộ narration.
2. Ghi timestamp của lỗi phát âm, mất từ, lặp từ hoặc nhịp không tự nhiên.
3. Chỉ sửa câu khi câu nói thật sự khó nghe hoặc phát âm sai; không thêm nội dung để kéo dài video.
4. Sau khi voice được duyệt, cập nhật timeline trong `Kich_Ban.md` và `Pormpt.md` theo timing thực từ manifest.

