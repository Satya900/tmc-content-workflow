from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_RIGHT
import pypdfium2 as pdfium

from tmc_fonts import find_fonts

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'/'pdf'; OUT.mkdir(parents=True,exist_ok=True)
QA=ROOT/'tmp'/'pdfs'/'costing'; QA.mkdir(parents=True,exist_ok=True)
FONTS=find_fonts()
pdfmetrics.registerFont(TTFont('Arial',str(FONTS['body'])))
pdfmetrics.registerFont(TTFont('ArialBold',str(FONTS['bold'])))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='ArialBold',italic='Arial',boldItalic='ArialBold')
styles=getSampleStyleSheet()
for name in ['Normal','BodyText','Title','Heading1','Heading2']:
    styles[name].fontName='Arial'; styles[name].textColor=colors.black
styles['BodyText'].fontSize=10; styles['BodyText'].leading=14; styles['BodyText'].spaceAfter=8
styles['Title'].fontName='ArialBold'; styles['Title'].fontSize=25; styles['Title'].leading=30; styles['Title'].spaceAfter=16
styles['Heading1'].fontName='ArialBold'; styles['Heading1'].fontSize=18; styles['Heading1'].leading=23; styles['Heading1'].spaceAfter=12
styles['Heading2'].fontName='ArialBold'; styles['Heading2'].fontSize=12; styles['Heading2'].leading=16; styles['Heading2'].spaceBefore=10; styles['Heading2'].spaceAfter=6
styles.add(ParagraphStyle(name='Cell',fontName='Arial',fontSize=9,leading=12))
styles.add(ParagraphStyle(name='SmallTMC',fontName='Arial',fontSize=8.5,leading=12,spaceAfter=6))
story=[]; source=[]
def p(t,style='BodyText'):
    story.append(Paragraph(t,styles[style])); source.append(t)
def h(t): p(t,'Heading2')
def page(title):
    if story: story.append(PageBreak())
    p(title,'Heading1'); source.append('\n')
def table(headers,rows,widths):
    data=[[Paragraph(escape(str(x)),styles['Cell']) for x in row] for row in [headers]+rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DFEEF3')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#D9D9D9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.extend([t,Spacer(1,10)])
    source.append(' | '.join(headers)); source.extend(' | '.join(map(str,r)) for r in rows)

p('TMC Content Platform','Title')
p('Development proposal and operating cost estimate','Heading1')
p('Prepared for The Modern Classroom<br/>27 September 2026 | Version 1')
p('This proposal covers a dedicated TMC web application for planning, drafting, reviewing and exporting non-video content. The fixed development fee is <b>₹2,00,000</b>, with delivery targeted within <b>one month</b> of scope approval and receipt of required inputs.')
p('TMC should budget <b>₹6,000–₹10,000 per month</b> for the core platform services. Optional publishing subscriptions and ongoing developer maintenance are separate. Human approval remains required before content is published.')
table(['Cost category','Proposed budget'],[
('One-time development','₹2,00,000'),('Core monthly operating budget','₹6,000–₹10,000'),('Core annual operating budget','₹72,000–₹1,20,000'),('First year including development','₹2,72,000–₹3,20,000')],[270,229])
p('All amounts exclude applicable taxes, foreign exchange fees and optional services. Annual figures assume 12 full months of operation. Operating budgets are estimates, not fixed-price or unlimited-use commitments.','SmallTMC')
h('What the investment delivers')
p('One workspace for TMC knowledge, content briefs, generated drafts, branded post templates, review history, exports and a content calendar. The existing TMC knowledge and skill materials will inform the application workflow.')
h('Planning basis')
p('One brand, 2–5 application users and approximately 25 non-video content placements per month, with moderate revisions. The build uses existing approved photographs and a limited template library. Video production and Ready for Umrah are outside this proposal.')
p('<b>Commercial status:</b> The development fee and one-month target reflect the current discussion. Scope quantities, milestone terms and support provisions below are proposed for agreement before kickoff. This web application proposal does not automatically amend or add to the earlier desktop-workflow agreement.')

page('Development scope and fee allocation')
p('The following allocation explains the fixed ₹2,00,000 development fee. It is a scope breakdown, not an hourly rate card or a menu of independently priced modules.')
table(['Workstream','Included work','Allocation'],[
('Requirements and design','Workflow specification, screen design and data model','₹20,000'),
('Application foundation','Login, roles, TMC knowledge and media records','₹35,000'),
('AI content workflow','Briefs, format prompts, draft generation, edits and versions','₹40,000'),
('Visual templates and exports','Three template families with PNG and PDF exports','₹35,000'),
('Review and job management','Approval states, calendar, job retries and notifications','₹30,000'),
('Testing and handover','Acceptance checks, deployment, training and documentation','₹40,000'),
('Total fixed development fee','','₹2,00,000')],[118,292,89])
h('Included content formats')
p('Founder and company LinkedIn posts, LinkedIn PDF carousels, Instagram static posts and carousels, Facebook adaptations, newsletter copy, blog drafts and website copy. A calendar entry is a planned placement. Drafting these formats does not include a monthly managed content service.')
h('Proposed template and editing limits')
p('Three visual template families: educational carousel, tour photo carousel and static announcement. Include square and portrait image variants where appropriate and a PDF carousel export. Users can edit text, select photographs and reorder slides through form controls. A freeform Canva-style design editor is excluded.')
h('Proposed workflow')
p('Brief and sources → draft generation → editorial checks → human review → approved version → branded export → calendar and publication record. Editing an approved draft requires fresh approval. Media records capture permission status, and unknown permission blocks use of identifiable student media.')
p('The base scope produces approved publishing assets. Direct social publishing, newsletter sending, CMS publishing and automated analytics ingestion require separately confirmed integrations.','SmallTMC')

page('Monthly operating cost breakdown')
p('Vendor prices were checked on 27 September 2026. INR conversions use a planning rate of ₹90 per US dollar, not a live exchange-rate quote. References appear on page 6.')
table(['Service','Purpose and pricing basis','Monthly INR'],[
('Vercel Pro [1]','Web hosting. $20 base for the initial setup. Extra paid seats and usage are additional.','₹1,800'),
('Supabase Pro [2]','Database, login and storage. $25 base with one small project covered by the compute credit.','₹2,250'),
('Claude API [3]','Usage-based content generation and editorial checks. Planning allowance, not a subscription quote.','₹500–₹2,500'),
('Trigger.dev [4]','Background jobs and rendering. Budget $10 Hobby plan with allowance for excess compute.','₹900–₹1,500'),
('Resend [5]','Application notifications. Start on free tier, with allowance for growth.','₹0–₹500'),
('Domain','Allowance averaged monthly. Existing TMC subdomain may avoid a new registration.','₹100–₹200'),
('Estimated core total','Sum of the above service allowances','₹5,550–₹8,750'),
('Recommended budget','Rounded budget with headroom for modest variation','₹6,000–₹10,000')],[105,300,94])
h('What does not require another subscription')
p('Next.js, TypeScript and the HTML/CSS rendering code carry no software subscription charge. Playwright rendering uses the background compute budget above. GitHub Free is suitable for the initial code repository within its allowances [6]. Database and media storage start within Supabase allowances.')
h('What can increase the bill')
p('Long source documents, repeated draft regeneration, more users or paid developer seats, additional database projects, accumulated photographs, large downloads and render jobs can increase usage. Generated images, research APIs and marketing email delivery are outside the base estimate.')
p('Production accounts should be owned and paid for by TMC. Configure usage alerts and available spending controls, then review actual consumption after the first month. Budget alerts are not a guarantee that every provider will stop charging at a fixed amount.','SmallTMC')

page('Optional services and annual scenarios')
table(['Option','Budget and billing','Scope condition'],[
('Buffer Essentials [7]','4 channels × $5/month = $20/month equivalent. ₹1,800/month or ₹21,600/year, billed annually.','Publishing subscription only. Integration development is separately scoped and format support must be tested.'),
('Bannerbear [8]','Starts at $49/month, approximately ₹4,410/month or ₹52,920/year.','Alternative rendering service. Not needed with the proposed custom renderer. Avoid purchasing both by default.'),
('Marketing email delivery','Separate quote based on contacts and send volume.','Newsletter copy is included. Campaign delivery, consent management and nurture automation are separate.'),
('Ongoing maintenance','Separate support agreement and fee.','Recurring fixes, dependency updates, monitoring and changes after the agreed support period.')],[112,189,198])
h('First year budget comparison')
table(['Scenario','Monthly operating budget','First year including build'],[
('Core platform','₹6,000–₹10,000','₹2,72,000–₹3,20,000'),
('Core plus Buffer subscription','₹7,800–₹11,800 equivalent','₹2,93,600–₹3,41,600')],[205,140,154])
p('The Buffer scenario adds ₹21,600 to the annual core budget. It does not include the cost of building or maintaining a publishing integration. Both scenarios exclude taxes, maintenance retainers, marketing email delivery and other optional work.','SmallTMC')
h('Operating cost ownership')
p('TMC pays vendor subscriptions and usage directly. The development fee covers the agreed implementation work, not recurring vendor bills. The developer’s normal coding tools and internal productivity subscriptions are part of the developer’s delivery overhead and are not separate client subscriptions under this proposal.')
h('Recommended starting configuration')
p('Launch with Vercel, Supabase, one AI API provider, Trigger.dev and the custom renderer. Use the notification service within its initial allowance. Add publishing only after the team has accepted the content and export workflow and the required formats have passed a live integration test.')

page('Delivery milestones and acceptance')
p('The one-month target starts after scope approval, the kickoff payment and access to required accounts, brand assets and source material. A nominated TMC reviewer should provide consolidated feedback within two working days. External approvals and delayed inputs may move the delivery date.')
table(['Period','Delivery milestone'],[
('Week 1','Confirm scope and templates. Build login, roles, knowledge records, media intake and the basic dashboard.'),
('Week 2','Implement format workflows, AI generation, editorial checks, editing, version history and review states.'),
('Week 3','Implement the three template families, PNG/PDF exports, job retries, notifications and calendar.'),
('Week 4','Run client acceptance checks, correct agreed defects, deploy, train the team and hand over source and documentation.')],[73,426])
h('Proposed payment schedule')
table(['Milestone','Share','Amount'],[
('Scope approval and kickoff','40%','₹80,000'),
('Working pilot accepted','30%','₹60,000'),
('Final acceptance and handover','30%','₹60,000'),
('Total','100%','₹2,00,000')],[310,70,119])
h('Acceptance checks')
p('The pilot must demonstrate a brief becoming an editable draft, a saved revision, a reviewer decision and an approved export. Final acceptance should cover at least one example of every included content format and each of the three visual template families.')
p('Also verify role access, rejection and revision handling, approval invalidation after edits, media permission blocking, failed-job recovery and readable PNG/PDF exports. AI checks assist the reviewer and do not certify that every generated statement is accurate.')
h('Handover')
p('Provide the application source, database structure, deployment instructions, account access handover, prompt and template configuration, and a team operating guide. Include one training session and an agreed backup and recovery procedure. TMC supplies a reviewer to complete acceptance.')

page('Commercial assumptions and references')
h('Proposed support and change terms')
p('Include 30 calendar days of correction for reproducible defects against the accepted scope after launch. New features, additional templates, content operations and third-party API changes are separate work. An ongoing maintenance retainer, response times and service hours require a separate agreement. These are proposed terms for confirmation, not previously accepted commitments.')
p('TMC supplies approved brand assets, factual source material, media permissions, account access and review decisions. Requested additions receive a written scope, price and timeline before work begins. No growth, engagement, lead-generation or time-saving outcome is guaranteed.')
h('Items outside the fixed fee')
p('Video and avatar workflows, Ready for Umrah, multiple brands, a freeform design editor, unlimited template revisions, bulk historical migration, paid advertising, direct CMS publishing, automated social analytics, research subscriptions and ongoing monthly content production. Social publishing and marketing email integrations are also excluded unless added in writing.')
h('Approval before kickoff')
p('Confirm the included formats and three template families, nominated reviewer, production account ownership, operating budget and payment/support terms. Confirm in writing how this proposal relates to any earlier ₹80,000 workflow agreement so neither party assumes an unagreed credit or additional charge. Applicable development taxes will be stated on the formal quotation or invoice.')
h('Official pricing references')
p('Vendor prices may change. Links below support subscription rates and billing structures. AI, domain and usage allowances in this proposal are estimates rather than vendor quotations. Checked 27 September 2026.','SmallTMC')
refs=[('1','Vercel','https://vercel.com/pricing'),('2','Supabase','https://supabase.com/pricing'),('3','Anthropic API pricing','https://platform.claude.com/docs/en/about-claude/pricing'),('4','Trigger.dev','https://trigger.dev/pricing'),('5','Resend','https://resend.com/pricing'),('6','GitHub','https://github.com/pricing'),('7','Buffer','https://buffer.com/pricing'),('8','Bannerbear','https://www.bannerbear.com/pricing/')]
for n,label,url in refs:
    p(f'[{n}] {label}: <link href="{url}" color="#0E7FA6">{url}</link>','SmallTMC')

def footer(c,d):
    c.setFont('Arial',8); c.setFillColor(colors.HexColor('#666666'))
    c.drawString(48,28,'TMC Content Platform | Cost proposal | 27 September 2026')
    c.drawRightString(547,28,str(d.page))
path=OUT/'TMC_Content_Platform_Cost_Proposal.pdf'
doc=SimpleDocTemplate(str(path),pagesize=(595,842),rightMargin=48,leftMargin=48,topMargin=43,bottomMargin=48,title='TMC Content Platform Development and Operating Costs',author='')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
(OUT/'TMC_Content_Platform_Cost_Proposal_source.txt').write_text('\n\n'.join(source),encoding='utf-8')
pdf=pdfium.PdfDocument(str(path))
for i,page_obj in enumerate(pdf):
    page_obj.render(scale=1.3).to_pil().save(QA/f'page-{i+1}.png')
print(f'Created {path} with {len(pdf)} pages')
