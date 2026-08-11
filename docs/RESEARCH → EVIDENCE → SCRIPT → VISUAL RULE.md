# RESEARCH → EVIDENCE → SCRIPT → VISUAL RULE

> **Version:** 1.1.0  
> **Last verified (editorial consistency):** 2026-08-11  
> **Status:** Working research and evidence standard; policy/product details require current official verification.

## Phạm vi tài liệu

Tài liệu này quản lý cách tìm nguồn, đánh giá evidence, xây claim ledger, lập visual plan và chuyển evidence thành annotated script. Nó không phải tư vấn pháp lý và không tự xác nhận một asset đủ điều kiện bản quyền, fair use, monetization hoặc disclosure.

Các tài liệu chuyên trách được áp dụng theo phạm vi: [Quy_trình.md](Quy_trình.md) quyết định thứ tự thao tác, [Check_List.md](Check_List.md) quyết định quality/policy gate, [Bố_Cục_prompt.md](Bố_Cục_prompt.md) quyết định cấu trúc prompt visual, [ElevenLabs.md](ElevenLabs.md) quyết định voice/TTS delivery và [Google.md](Google.md) quyết định yêu cầu Google/YouTube hiện hành. Các tài liệu chuyên trách được ưu tiên trong phạm vi của chúng.

> **Lưu ý định hướng 2.0:** Các đoạn data center/power grid trong tài liệu này là case study cũ để minh họa phương pháp evidence, claim ledger và annotated script. Chúng không còn là topic direction. Khi áp dụng, thay case study bằng một hiện tượng thuộc Strange Nature, Animal Mysteries, Human Body, Everyday Physics, Scientific Mysteries hoặc Extreme Earth.

## 1. MỤC TIÊU

AI không được tạo kịch bản bằng cách tổng hợp ngẫu nhiên thông tin trên Internet.

Mỗi video phải được xây dựng theo chuỗi:

**Question → Research → Evidence → Interpretation → Story → Visual Evidence → Final Script**

Nguyên tắc cốt lõi:

**EVIDENCE BEFORE NARRATIVE**

Không được quyết định trước một kết luận hấp dẫn rồi tìm các nguồn chỉ để chứng minh kết luận đó.

Phải nghiên cứu trước, xác định bằng chứng, mâu thuẫn, uncertainty và counterpoint, sau đó mới xây dựng narrative.

Mỗi video cuối cùng phải cho người xem cảm giác:

**This was researched and produced.**

Không phải:

**This was generated.**

---

# 2. NGUYÊN TẮC NGUỒN

Không dùng một nhãn Tier duy nhất để thay thế đánh giá nguồn. Mỗi source phải được đánh giá theo ít nhất ba trục độc lập:

- **Provenance:** PRIMARY / SECONDARY / AGGREGATOR.
- **Independence:** INDEPENDENT / SELF-INTERESTED / UNKNOWN.
- **Methodology:** STRONG / ADEQUATE / WEAK / NOT DISCLOSED.

Tier bên dưới chỉ là ưu tiên khởi đầu. Một tài liệu primary có thể vẫn self-interested hoặc có methodology yếu; một nguồn secondary tốt có thể là corroboration độc lập quan trọng.

## SOURCE TIER S — PRIMARY / AUTHORITATIVE CANDIDATES

Ưu tiên cao nhất để truy xuất bằng chứng gốc, nhưng không mặc nhiên đúng, độc lập hoặc phù hợp với mọi claim.

Bao gồm:

- Cơ quan chính phủ.
- Cơ quan quản lý.
- Official statistics.
- Court documents.
- Laws and regulations.
- Grid operators.
- Utility filings.
- SEC filings.
- Company annual reports.
- Earnings reports.
- Investor presentations.
- Official technical reports.
- Research papers gốc.
- Original datasets.
- University research.
- Official transcripts.
- Official speeches hoặc testimony.
- Official project documents.

Ví dụ tùy chủ đề:

EIA, DOE, FERC, NERC, PJM, ERCOT, SEC, Census Bureau, BLS, EPA, DOT, FAA, Federal Reserve, Congressional Research Service, Lawrence Berkeley National Laboratory, national laboratories, utility commissions...

Nếu có nguồn primary phù hợp thì phải ưu tiên nguồn đó hơn bài báo viết lại về cùng dữ liệu.

Company filing, investor presentation, official statement hoặc testimony là primary đối với điều tổ chức/cá nhân đã công bố, nhưng thường là **SELF-INTERESTED** đối với claim về hiệu quả, tác động hoặc tranh chấp. Phải kiểm tra methodology và tìm corroboration độc lập khi claim quan trọng.

---

## SOURCE TIER A — HIGH-QUALITY SECONDARY

Có thể sử dụng để:

- Tìm context.
- Tìm câu chuyện.
- Tìm nhân vật.
- Tìm chronology.
- Phát hiện vấn đề cần research sâu hơn.
- Xác nhận cách các bên khác nhau nhìn nhận vấn đề.

Bao gồm:

- Reuters.
- Associated Press.
- Financial Times.
- Bloomberg.
- Wall Street Journal.
- New York Times.
- BBC.
- CNBC.
- Major specialist publications có editorial standards rõ ràng.
- Các viện nghiên cứu uy tín.

Một bài báo Tier A không nên thay thế nguồn primary khi bài báo đang dẫn lại dữ liệu mà nguồn primary vẫn truy cập được.

---

## SOURCE TIER B — SPECIALIST / INDUSTRY

Có thể dùng khi tác giả hoặc publication có chuyên môn rõ ràng.

Ví dụ:

- Trade publications.
- Industry analysis.
- Engineering publications.
- Energy publications.
- Semiconductor publications.
- Construction publications.
- Logistics publications.

Phải xác định:

- Ai xuất bản?
- Ai tài trợ?
- Có conflict of interest không?
- Họ đang báo cáo fact hay đưa opinion?
- Dữ liệu gốc của họ đến từ đâu?

---

## SOURCE TIER C — DISCOVERY ONLY

Bao gồm:

- Blog cá nhân.
- Medium.
- Reddit.
- X/Twitter.
- Facebook.
- YouTube commentary/video tổng hợp của bên thứ ba.
- Forums.
- Wikipedia.
- SEO websites.
- AI-generated articles.
- Aggregator sites.

Các nguồn này có thể dùng để **phát hiện câu hỏi**, nhưng không được dùng làm bằng chứng chính cho factual claim quan trọng.

Nếu Tier C đưa ra một claim đáng chú ý, AI phải truy ngược về original source.

Không phân loại chỉ dựa trên platform: video phiên điều trần, bản ghi chính phủ, phỏng vấn gốc hoặc footage do chủ thể trực tiếp công bố có thể là primary artifact. Khi đó vẫn phải đánh giá independence, context, transcript/timecode và quyền sử dụng.

---

# 3. SOURCE PRIORITY RULE

Khi nhiều nguồn cùng nói về một dữ kiện, ưu tiên theo thứ tự:

**Original Data → Primary Document → Official Statement → Peer-reviewed / Institutional Research → High-quality Journalism → Specialist Publication → Everything Else**

Không được cite một bài báo nếu bài báo chỉ đang cite một báo cáo gốc mà báo cáo gốc có thể truy cập.

Ví dụ:

Không ưu tiên:

“Reuters reports that EIA estimates...”

nếu có thể dùng trực tiếp:

“EIA estimates...”

Reuters vẫn có thể được sử dụng để cung cấp context hoặc reaction.

---

# 4. FRESHNESS RULE

Mỗi nguồn phải lưu:

- Publication date.
- Data period.
- Last updated date nếu có.
- Date accessed.
- Forecast horizon nếu là dự báo.

AI phải phân biệt:

**Published recently ≠ data is recent.**

Một báo cáo xuất bản năm 2026 nhưng dùng dữ liệu năm 2023 phải được ghi rõ.

Đối với:

- AI.
- Energy.
- Data centers.
- Technology.
- Company information.
- Laws.
- Regulations.
- Prices.
- Forecasts.
- Current projects.

AI phải ưu tiên tài liệu mới nhất có thể tìm được.

Nhưng không được bỏ qua nguồn cũ nếu nó cần thiết để giải thích lịch sử hoặc so sánh xu hướng.

Các trường freshness này phải xuất hiện trong cả Evidence Object và Source Table; nếu không áp dụng, ghi `N/A` thay vì bỏ trống.

---

# 5. MULTI-SOURCE VERIFICATION

Một claim quan trọng không được chấp nhận chỉ vì có một website viết về nó.

Đối với claim có ảnh hưởng lớn đến luận điểm chính, AI nên tìm:

**1 primary source**

và khi có thể:

**1 independent corroborating source.**

Nếu các nguồn mâu thuẫn:

KHÔNG chọn nguồn thuận lợi nhất cho narrative.

Phải ghi:

**SOURCE CONFLICT**

và giải thích:

- Nguồn A nói gì.
- Nguồn B nói gì.
- Vì sao có thể khác nhau.
- Dataset hoặc methodology có khác không.
- Khoảng thời gian có khác không.
- Điều gì hiện vẫn chưa chắc chắn.

---

# 6. KHÔNG ĐƯỢC DÙNG AI SEARCH RESULT LÀM SOURCE

Search engine summary, AI Overview, chatbot answer hoặc snippet chỉ được xem như:

**Discovery Layer**

Không phải evidence.

AI phải mở original source trước khi sử dụng claim.

Không được viết:

“According to search results...”

Phải xác định publisher thực sự và tài liệu thực sự.

---

# 7. EVIDENCE OBJECT

Mỗi bằng chứng được tìm thấy phải tạo thành một Evidence Object.

Cấu trúc:

**Evidence ID:** E001

**Claim:**  
Claim mà nguồn hỗ trợ.

**Epistemic Type:**  
FACT / ESTIMATE / FORECAST / OPINION / INFERENCE

**Narrative Role:**  
SUPPORT / COUNTERPOINT / CONTEXT / UNCERTAINTY

**Source Tier:**  
S / A / B / C

**Provenance / Independence / Methodology:**  
Ba đánh giá độc lập theo nguyên tắc nguồn ở trên.

**Publisher:**  
Tên tổ chức.

**Document:**  
Tên tài liệu.

**Author:**  
Nếu có.

**Publication Date:**  
Ngày xuất bản.

**Last Updated Date:**  
Ngày cập nhật gần nhất nếu có; nếu không có ghi N/A.

**Data Period:**  
Khoảng thời gian dữ liệu.

**Date Accessed:**  
Ngày mở và kiểm tra original source.

**Forecast Horizon:**  
Mốc dự báo nếu là forecast; nếu không áp dụng ghi N/A.

**URL:**  
Original URL.

**Page / Section:**  
Page, table, figure hoặc section chứa bằng chứng.

**Supporting Passage:**  
Một đoạn ngắn đủ để kiểm chứng claim.

**Numbers:**  
Các con số liên quan.

**Units:**  
MW, GW, TWh, USD, %, years...

**Confidence:**  
HIGH / MEDIUM / LOW

**Counter Evidence:**  
Nguồn hoặc dữ kiện phản bác nếu tồn tại.

**Visual Available:**  
YES / NO

**Rights Status:**  
PUBLIC DOMAIN / CC / LICENSED / PERMISSION / FAIR-USE-CANDIDATE / UNKNOWN

---

# 8. FACT / INFERENCE SEPARATION

AI bắt buộc phân biệt **Epistemic Type** với **Narrative Role**. SOURCED FACT và INFERENCE mô tả trạng thái tri thức; COUNTERPOINT mô tả vai trò trong lập luận; UNCERTAINTY là qualifier phải được giữ xuyên suốt claim, script và visual.

## SOURCED FACT

Thông tin được nguồn trực tiếp hỗ trợ.

Ví dụ:

“Data centers consumed X TWh of electricity.”

---

## INFERENCE

Kết luận hợp lý được suy ra từ nhiều evidence.

Ví dụ:

“This suggests electricity availability may become more important than cheap land for some data center projects.”

Không được biến inference thành:

“Electricity is now more important than land.”

trừ khi có bằng chứng đủ mạnh.

---

## COUNTERPOINT

Evidence có khả năng làm yếu hoặc thay đổi luận điểm chính.

Counterpoint không được loại bỏ chỉ vì nó làm câu chuyện bớt dramatic.

---

## UNCERTAINTY

Thông tin:

- Chưa chắc chắn.
- Có forecast range lớn.
- Có nhiều methodology.
- Chưa có dữ liệu đầy đủ.
- Có tranh luận giữa chuyên gia.

Phải được trình bày đúng mức độ certainty.

Không dùng ngôn ngữ tuyệt đối cho forecast.

---

# 9. CLAIM LEDGER

Trước khi viết final script, AI phải tạo một Claim Ledger.

Ví dụ:

C01  
“U.S. electricity demand is accelerating.”

Supported by: E001, E004

C02  
“Data centers are one important contributor.”

Supported by: E002, E005

C03  
“Transmission construction cannot always keep pace.”

Supported by: E007, E008

C04  
“This mismatch could move data center investment geographically.”

Type: INFERENCE

Supported by: E002 + E007 + E010

Mọi factual statement quan trọng trong script phải map được về ít nhất một Evidence ID.

---

# 10. VISUAL EVIDENCE RULE

AI không chỉ tìm thông tin.

AI phải tìm **visual evidence**.

Ưu tiên các asset có khả năng vừa:

**chứng minh claim**

vừa:

**tạo visual storytelling.**

Các loại asset nên tìm:

- Chart.
- Graph.
- Map.
- Satellite image.
- Table.
- Diagram.
- Report page.
- Government document.
- Company filing.
- Newspaper front page.
- Historical photograph.
- Infrastructure photograph.
- Project rendering.
- Official video footage.
- Government footage.
- Public-domain imagery.

---

# 11. DOCUMENT VISUAL RULE

Khi một tài liệu quan trọng chứa bằng chứng tốt, không nên chỉ đọc số liệu bằng voice-over.

Hãy xem tài liệu đó như một visual asset.

Ví dụ:

Narration:

“PJM's own forecast shows electricity demand accelerating.”

Visual:

Full report cover

→ zoom vào tên báo cáo

→ chuyển tới page chứa chart

→ highlight đường forecast

→ zoom vào con số quan trọng

→ hiện nguồn nhỏ ở cạnh dưới màn hình.

Đây là:

**Document-as-Evidence Storytelling**

Người xem không chỉ nghe narrator nói.

Họ nhìn thấy bằng chứng.

---

# 12. DOCUMENT SCREENSHOT RULE

Mỗi screenshot từ report phải lưu:

- Document title.
- Publisher.
- Publication date.
- Page number.
- Figure/table number.
- Original caption.
- URL.
- Screenshot coordinates nếu cần.
- Rights status.
- Intended use.

Không crop mất:

- Axis.
- Units.
- Legend.
- Source note.
- Relevant labels.

nếu những thành phần đó cần để hiểu chart.

Có thể crop để dựng video nhưng không được crop theo cách làm thay đổi ý nghĩa.

---

# 13. IMAGE RIGHTS RULE

Việc một hình ảnh xuất hiện công khai trên Internet KHÔNG đồng nghĩa hình đó được tự do sử dụng.

Ưu tiên:

**Public Domain**

→ **Explicitly Licensed**

→ **Creative Commons compatible with intended use**

→ **Permission obtained**

→ sau đó mới xem xét copyrighted material trong bối cảnh commentary, criticism, reporting hoặc documentary.

Fair use không được coi là một giấy phép tự động.

Việc dùng asset để **transition**, crop, animate, thêm voice-over hoặc chỉnh sửa hình ảnh không tự tạo license và không tự chứng minh fair use. `TRANSITION` chỉ mô tả chức năng kể chuyện; quyền sử dụng vẫn phải được xác nhận độc lập theo từng asset trước production.

Nếu quyền sử dụng không rõ:

**RIGHTS STATUS = UNKNOWN**

và asset không nên được đưa vào production tự động.

Đặc biệt:

Một PDF của cơ quan chính phủ có thể chứa:

- Third-party photo.
- Licensed map.
- Contractor illustration.
- Copyrighted figure.

Do đó AI phải kiểm tra credit/caption của từng asset.

“Government footage/document” cũng không mặc nhiên public domain: phải kiểm tra cơ quan liên bang hay state/local, credit của contractor/third party, điều khoản sử dụng và từng thành phần nằm trong tài liệu.

---

# 14. SOURCE VISUAL TRANSFORMATION RULE

Không nên lấy hàng loạt footage/hình của người khác rồi ghép lại dưới AI voice.

Mỗi external visual phải có ít nhất một vai trò cụ thể:

**EVIDENCE**

hoặc

**EXPLANATION**

hoặc

**CRITICISM**

hoặc

**CONTEXT**

hoặc

**COMPARISON**

hoặc

**TRANSITION — chỉ khi asset đã có quyền sử dụng độc lập**

Nếu asset không đóng góp gì ngoài việc “có hình để màn hình không trống”, nên tìm visual khác.

External material phải được kết hợp với:

- Original narration.
- Original storyline.
- Analysis.
- Motion.
- Highlight.
- Annotation.
- Comparison.
- Diagram.
- Editing.
- Context.

để video thể hiện rõ giá trị biên tập nguyên bản.

Các biến đổi biên tập trên giúp thể hiện originality nhưng không thay thế permission/license và không bảo đảm fair use hoặc monetization. Asset có `RIGHTS STATUS = UNKNOWN` phải đi qua [Check_List.md](Check_List.md), không được auto-approved.

---

# 15. VISUAL TRUTH HIERARCHY

Visual nên ưu tiên theo thứ tự:

### Level 1 — EVIDENCE VISUAL

Chart, map, document, dataset, official image.

### Level 2 — REAL-WORLD VISUAL

Footage hoặc photography về địa điểm, công trình, con người hoặc hệ thống thực.

### Level 3 — EXPLANATORY VISUAL

Diagram, map animation, chart animation, typography, motion graphics.

### Level 4 — AI VISUAL

Synthetic imagery để:

- Conceptualize.
- Reconstruct.
- Illustrate.
- Transition.
- Create atmosphere.

AI visual không được thay thế evidence visual khi evidence thật tồn tại.

---

# 16. AI IMAGE RULE

AI image/video nên được sử dụng khi:

- Không có footage phù hợp.
- Cần visual metaphor.
- Cần conceptual visualization.
- Cần minh họa tương lai hoặc scenario giả định.
- Cần reconstruction.
- Cần transitional imagery.
- Một hệ thống không thể quay trực tiếp.

Không sử dụng AI image như bằng chứng rằng một sự kiện đã xảy ra.

Nếu AI tạo:

- Data center.
- Power plant.
- Explosion.
- Flood.
- Protest.
- Factory.
- City.
- Person.
- Historical event.

theo phong cách photorealistic, không được dựng theo cách khiến người xem nghĩ đó là footage thật của sự kiện nếu thực tế không phải vậy.

Nếu realistic synthetic media thuộc trường hợp YouTube yêu cầu disclosure, production pipeline phải đánh dấu:

**AI DISCLOSURE REQUIRED = YES**

---

# 17. VISUAL MIX

Các tỷ lệ dưới đây chỉ là **working heuristic để lập kế hoạch**, không phải yêu cầu YouTube, công thức monetization hay tỷ lệ tối ưu đã được chứng minh. Không dùng tỷ lệ cứng.

Nhưng với documentary thông thường, starting guideline có thể là:

**50–70%**  
Real footage + documentary evidence + photographs + source material.

**15–30%**  
Maps + charts + diagrams + motion graphics.

**10–25%**  
AI-generated visual / reconstruction / conceptual imagery.

Đây không phải quota.

Nếu một video có rất nhiều footage thật tốt, AI imagery có thể gần bằng 0.

Nếu chủ đề khó hình dung hoặc mang tính tương lai, AI visual có thể tăng.

Nguyên tắc:

**Reality first. AI second.**

---

# 18. KHÔNG DÙNG VISUAL THEO KIỂU SLIDESHOW

Cấm pattern:

AI voice

→ image

→ zoom

→ image

→ zoom

→ image

→ zoom.

Visual phải có chức năng kể chuyện.

Ví dụ:

Satellite map

→ zoom vào Northern Virginia

→ highlight cluster data centers

→ cut sang footage thật

→ transmission infrastructure

→ official chart

→ document screenshot

→ diagram giải thích bottleneck

→ AI conceptual visual

→ quay lại footage thật.

---

# 19. SCRIPT PHILOSOPHY

Script không phải research report.

Research phải chặt chẽ.

Script phải tự nhiên.

Người xem không cần nghe:

“According to source A... According to source B... According to source C...”

Mà nên nghe câu chuyện.

Evidence được tích hợp tự nhiên vào narrative.

Ví dụ:

Không nên:

“According to PJM's 2026 forecast, demand is increasing.”

Tốt hơn:

“For nearly two decades, electricity demand barely moved. Now that line is bending upward again.”

Visual:

Historical load chart.

Sau đó:

“And one of the biggest new loads doesn't look like a factory.”

Cut:

Data center.

“It's a building filled with computers.”

Evidence và storytelling đi cùng nhau.

---

# 20. SCRIPT STRUCTURE

Không dùng template cứng nhắc cho mọi video.

Sử dụng một **Elastic Narrative Structure**.

Mỗi video có thể thay đổi bố cục, nhưng nên đi qua các narrative functions sau.

---

## PHASE 1 — COLD OPEN

Khoảng 0:00–0:30.

Mục tiêu:

Tạo một unanswered question.

Cold open nên chứa một hoặc nhiều yếu tố:

- Paradox.
- Conflict.
- Surprising number.
- Strange location.
- Unexpected consequence.
- Strong visual.
- Mystery.

Không bắt đầu bằng:

“Welcome back to the channel.”

Không bắt đầu bằng:

“In today's video we are going to talk about...”

Không bắt đầu bằng lịch sử dài.

---

## PHASE 2 — PROMISE

Cho người xem hiểu:

**Video này sẽ giải đáp điều gì?**

Không cần nói trực tiếp.

Có thể tạo promise bằng câu hỏi.

Ví dụ:

“America has power plants. It has fuel. It has money. So why are some of the world's richest technology companies struggling to find electricity?”

Sau câu này, người xem biết mystery cần được giải.

---

# 21. SCALE

Cho người xem thấy:

**Tại sao câu chuyện này đáng quan tâm?**

Dùng:

- Number.
- Map.
- Money.
- Population.
- Distance.
- Electricity.
- Physical scale.
- Growth rate.

Nhưng không dump quá nhiều statistics.

Một con số lớn nên được chuyển thành điều người xem có thể hình dung.

---

# 22. SYSTEM EXPLANATION

Chỉ giải thích hệ thống sau khi người xem đã biết vì sao họ cần hiểu nó.

Không:

“First, let's explain how the electrical grid works.”

Thay vào đó:

“To understand why a data center can wait years for power, you need to understand one strange feature of the grid.”

Bây giờ explanation phục vụ mystery.

---

# 23. FIRST REVEAL

Video cần sớm đưa cho người xem một phần đáp án.

Không kéo mystery quá lâu.

Ví dụ:

“The problem isn't necessarily that America can't generate enough electricity.”

Pause.

“The problem is where that electricity exists — and how quickly it can be moved.”

Đây là payoff đầu tiên.

Nhưng payoff này tạo câu hỏi tiếp theo:

“Tại sao không thể đơn giản truyền điện tới đó?”

---

# 24. ESCALATION

Mỗi answer nên mở ra một deeper problem.

Ví dụ:

AI demand

→ electricity demand

→ grid connection

→ transmission

→ transformers

→ permitting

→ utility investment

→ electricity prices.

Narrative phải có cảm giác đang đi sâu hơn vào hệ thống.

---

# 25. EVIDENCE BEAT

Sau các đoạn explanation dài, nên đưa một evidence moment.

Ví dụ:

- Map.
- Chart.
- Filing.
- Document.
- Case study.
- Satellite image.
- Interview.
- Quote.
- Comparison.

Evidence beat tạo cảm giác:

**“Đây không chỉ là narrator đang kể.”**

---

# 26. CASE STUDY

Abstract system trở nên dễ hiểu hơn khi có một location, company hoặc project cụ thể.

Ví dụ:

Không nói về “data centers in America” suốt 15 phút.

Có thể đi vào:

Northern Virginia.

Một utility.

Một county.

Một proposed data center.

Một power project.

Một transmission line.

Sau đó zoom trở lại national picture.

Pattern:

**Macro → Micro → Macro**

rất phù hợp với documentary.

Đây là framing phù hợp khi scale toàn hệ thống là hook. Nếu một location/person/project cụ thể tạo cold open mạnh hơn, có thể dùng **Micro → Macro → Micro** theo tài liệu phong cách viết; chỉ chọn pattern phục vụ central question.

---

# 27. MID-VIDEO TURN

Khoảng giữa video nên có một discovery làm thay đổi cách người xem nhìn câu chuyện.

Ví dụ:

Ban đầu:

“AI needs too much electricity.”

Sau research:

“But electricity generation isn't actually the entire problem.”

Turn:

“The bottleneck is increasingly the infrastructure between generation and demand.”

Một good turn giúp video không trở thành lecture tuyến tính.

---

# 28. COUNTERPOINT

Trước khi conclusion, phải kiểm tra:

“Điều gì có thể khiến thesis của video sai hoặc quá đơn giản?”

Ví dụ:

- New generation coming online.
- Efficiency improvements.
- Data center flexibility.
- New transmission.
- Regulatory reform.
- Forecast uncertainty.

Counterpoint làm conclusion đáng tin hơn.

---

# 29. CONSEQUENCE

Giải thích:

**So what?**

Ảnh hưởng có thể là:

- Electricity bill.
- Jobs.
- Investment.
- City growth.
- Company costs.
- Reliability.
- Technology development.
- Geography.
- Environment.
- Consumers.

Technical problem phải được kết nối trở lại với con người hoặc economic consequence.

---

# 30. CONCLUSION

Conclusion phải trả lời câu hỏi mở đầu.

Không chỉ summarize video.

Không:

“So today we learned about the power grid...”

Thay vào đó:

“America probably isn't running out of electricity. But the AI boom is exposing something more difficult to fix: power has to exist in the right place, at the right time, behind infrastructure that can take years to build.”

Conclusion có thể nuanced.

Không cần cố tạo dramatic answer nếu evidence không hỗ trợ.

---

# 31. OPEN ENDING

Nếu phù hợp, kết thúc bằng một implication lớn hơn.

Ví dụ:

“And that may change where the next generation of the Internet gets built.”

Đây là một câu kết mở rộng thế giới của video thay vì lặp lại introduction.

---

# 32. RETENTION RULE

Mỗi đoạn trong script phải trả lời câu hỏi:

**Why should the viewer keep watching the next 30 seconds?**

Nếu một đoạn chỉ tồn tại vì:

“Thông tin này đúng và tôi đã research nó”

thì chưa đủ.

Nó phải phục vụ ít nhất một chức năng:

- Advance mystery.
- Explain cause.
- Reveal evidence.
- Raise stakes.
- Change interpretation.
- Answer a question.
- Create another question.

---

# 33. OPEN LOOP RULE

Có thể tạo open loop.

Ví dụ:

“But that created another problem — one that money alone couldn't solve.”

Sau đó payoff phải xuất hiện trong thời gian hợp lý.

Không spam artificial cliffhanger.

Không giữ thông tin vô lý chỉ để kéo retention.

Curiosity phải đến từ story, không phải manipulation.

---

# 34. PACING RULE

Không quy định:

“phải đổi shot mỗi 3 giây.”

Thay đổi visual khi:

- Ý tưởng thay đổi.
- Scale thay đổi.
- Location thay đổi.
- Evidence xuất hiện.
- Narration chuyển từ abstract sang concrete.
- Một visual đã truyền tải xong thông tin.

Một chart phức tạp có thể cần 15 giây.

Một establishing shot có thể chỉ cần 3 giây.

**Information determines pacing.**

---

# 35. SENTENCE RULE

Narration phải được viết để NGHE, không phải để ĐỌC.

Ưu tiên:

- Câu ngắn.
- Câu rõ.
- Active voice.
- Concrete language.
- Natural contractions nếu phù hợp.
- Varied sentence length.
- Strategic pauses.

Tránh:

- Academic prose.
- Corporate jargon.
- Excessive adjectives.
- Repetitive transitions.
- Long nested sentences.

---

# 36. NUMBER RULE

Không bombard người xem bằng số.

Mỗi con số phải trả lời một trong các câu hỏi:

- How big?
- How fast?
- How expensive?
- How unusual?
- Compared with what?

Khi có thể:

**Raw number + comparison.**

Ví dụ:

Không chỉ:

“649 TWh.”

Mà:

“649 terawatt-hours — several times the electricity data centers consumed only a few years earlier.”

Mọi comparison vẫn phải được verify.

---

# 37. NO HYPE RULE

Cấm tự động sử dụng:

- “This changes everything.”
- “America is doomed.”
- “Nobody is talking about this.”
- “The shocking truth.”
- “This will destroy...”
- “Everything you know is wrong.”
- “The biggest crisis ever.”

trừ khi evidence thực sự hỗ trợ mức độ khẳng định đó.

Curiosity không đồng nghĩa sensationalism.

---

# 38. TITLE / SCRIPT CONSISTENCY

30 giây đầu phải thực hiện promise của:

**Title + Thumbnail**

Nếu title là:

“Why Some AI Data Centers Can't Get Power Fast Enough”

script không được dành hai phút đầu kể lịch sử của Internet.

Người xem phải nhanh chóng thấy:

AI.

Power.

Conflict.

---

# 39. ORIGINALITY RULE

Final video không được trở thành:

**Collection of other people's material + AI voice.**

Originality phải thể hiện trong:

- Research question.
- Source synthesis.
- Story structure.
- Argument.
- Narration.
- Data interpretation.
- Visual sequencing.
- Original charts.
- Original maps.
- Original diagrams.
- Commentary.
- Editing.
- Conclusion.

Third-party material hỗ trợ story.

Third-party material không phải story.

---

# 40. OUTPUT FORMAT CỦA AI

Sau research, AI không được chỉ trả về lời thoại, nhưng cũng không được sinh một file riêng cho mỗi gate. Sáu nhóm dữ liệu bắt buộc được hợp nhất vào đúng hai tài liệu Markdown chính của mỗi ngôn ngữ.

## A. KICH_BAN.MD — NỘI DUNG VÀ EVIDENCE

`Kich_Ban.md` phải chứa:

1. **Discovery verdict trong metadata/hướng đi chung:** main answer, strongest evidence, biggest conflict/uncertainty và story angle.
2. **Evidence & Sources table:** Source ID, title, publisher/author, publication/update/data/access dates khi liên quan, URL, tier, provenance, relevant location, reliability, independence/methodology và status.
3. **Claim mapping:** mỗi important claim map tới Source/Evidence ID, epistemic type, confidence và review status.
4. **Script timeline:** đúng năm cột `Thời lượng · Bố cục · Hình ảnh/B-Roll · Lời thoại/Voiceover · SFX/Notes`; cột Voiceover chứa toàn bộ clean narration.
5. **Human review flags:** claim cần kiểm tra, conflict chưa giải quyết, inference, pronunciation và story/fact sign-off.

## B. PORMPT.MD — VISUAL, PROMPT VÀ RIGHTS

`Pormpt.md` phải chứa:

1. **Master media map:** timestamp, visual purpose, loại REAL/AI/DOCUMENT/MOTION GRAPHIC, duration dùng cuối, source/prompt ID, transition vào/ra và status.
2. **Visual asset plan:** asset thật có direct item URL; tài liệu có source/page; AI có label `[AI-NOT-EVIDENCE]` và factual guardrail.
3. **Prompt AI đầy đủ:** timed action, composition, camera, continuity, constraints, reference ownership, model/date/output và QA.
4. **Asset registry:** owner, license, commercial/derivative rights, attribution, proof, AI provenance, disclosure và APPROVED/HOLD/REJECT.
5. **Human review flags:** asset chưa rõ quyền, AI cần disclosure, continuity/factual issue và visual/release sign-off.

Source Table, Evidence Ledger, Visual Asset Plan, annotated script và Human Review Flags vẫn là thành phần bắt buộc về dữ liệu; chúng không còn là sáu file/deliverable độc lập.

---

# 41. SCRIPT ANNOTATION TAGS

Sử dụng thống nhất:

[VO]

Narration.

[VISUAL-REAL]

Real footage/photo.

[VISUAL-DOC]

Original document, chart, report, filing.

[VISUAL-MAP]

Map / satellite.

[VISUAL-DATA]

Chart / data visualization.

[VISUAL-AI]

AI-generated image/video.

[AI-NOT-EVIDENCE]

Synthetic visual chỉ dùng minh họa.

[EVIDENCE: E000]

Evidence supporting narration.

[ON-SCREEN]

Text displayed.

[SOURCE]

Attribution displayed.

[COUNTERPOINT]

Alternative interpretation.

[UNCERTAINTY]

Uncertain information.

[RIGHTS-CHECK]

Asset chưa xác nhận quyền sử dụng.

---

# 42. FINAL QUALITY GATE

Không cho phép chuyển script sang production nếu bất kỳ điều nào sau đây vẫn tồn tại:

Important claim không có source.

Important number không có source.

Quote không xác định được original source.

Source chỉ là AI/search snippet.

Chart không rõ publisher.

Screenshot không lưu page/source.

Asset không rõ quyền sử dụng nhưng được đánh dấu auto-approved.

AI image đang bị sử dụng như historical/documentary evidence.

Narrative bỏ qua counterevidence quan trọng.

Title đưa ra claim mạnh hơn evidence.

Script có conclusion đã được quyết định trước research.

Quá nhiều external footage nhưng quá ít original analysis.

Video phụ thuộc vào AI imagery mặc dù có documentary evidence tốt hơn.

---

# 43. MASTER PRINCIPLE

Mỗi scene nên ưu tiên theo thứ tự:

**SHOW THE REAL THING**

nếu không:

**SHOW THE EVIDENCE**

nếu không:

**EXPLAIN IT VISUALLY**

nếu không:

**ILLUSTRATE IT WITH AI**

Không bắt đầu từ:

“AI có thể tạo hình gì cho câu narration này?”

Hãy bắt đầu từ:

“Có bằng chứng hoặc thứ gì trong thế giới thật mà người xem nên nhìn thấy không?”

---

# 44. STORY PRINCIPLE

Research phải làm video:

**TRUE**

Storytelling phải làm video:

**INTERESTING**

Visual evidence phải làm video:

**BELIEVABLE**

Editing phải làm video:

**WATCHABLE**

AI phải làm quá trình:

**FASTER**

AI không được thay thế bốn yếu tố đầu tiên.
