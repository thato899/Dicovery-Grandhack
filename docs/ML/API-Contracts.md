<html>
<body>
<!--StartFragment--><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">text</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span></span>
<span>---</span>
<span></span>
<span>## Page 3: API-Contracts</span>
<span></span>
<span>```markdown</span>
<span># API Contracts</span>
<span></span>
<span>## What are API Contracts?</span>
<span></span>
<span>**API contracts** define exactly how the ML model communicates with the backend and mobile app.</span>
<span></span>
<span>Think of it as a **handshake agreement**:</span>
<span>- "You send me this format"</span>
<span>- "I'll send you back that format"</span>
<span>- "If you send wrong format, I'll tell you"</span>
<span></span>
<span>&gt; **Why this matters:** Clear contracts prevent integration bugs and make development faster.</span>
<span></span>
<span>---</span>
<span></span>
<span>## For Different Team Members</span>
<span></span>
<span>| Role | What to Look For |</span>
<span>|------|------------------|</span>
<span>| **ML Engineer** | Implement these endpoints |</span>
<span>| **Backend Developer** | Call these endpoints |</span>
<span>| **Mobile Developer** | Understand response format |</span>
<span>| **QA/Testing** | Validate request/response |</span>
<span></span>
<span>---</span>
<span></span>
<span>## Part 1: Risk Prediction Endpoint</span>
<span></span>
<span>### 1.1 Endpoint Details</span>
<span></span>
<span>| Property | Value |</span>
<span>|----------|-------|</span>
<span>| **Method** | POST |</span>
<span>| **Path** | `/api/v1/predict/risk` |</span>
<span>| **Content-Type** | `application/json` |</span>
<span>| **Authentication** | API Key (header: `X-API-Key`) |</span>
<span>| **Rate Limit** | 100 requests/minute |</span>
<span></span>
<span>### 1.2 Request Schema</span>
<span></span>
<span>```json</span>
<span>{</span>
<span>    "latitude": -26.195,</span>
<span>    "longitude": 28.034,</span>
<span>    "timestamp": "2026-06-01T21:30:00+02:00",</span>
<span>    "crowd_density": 0.4,</span>
<span>    "lighting_score": 0.6</span>
<span>}</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong style="font-weight: 600;"><span class="">Field Descriptions:</span></strong></p><div class="ds-scroll-area ds-scroll-area--show-on-focus-within ds-scroll-area--enabled _1210dd7 c03cafe9" style="--dsl-scroll-area-gutters-disappear-delay: 1s; z-index: 0; position: relative; overflow: auto; scrollbar-width: none; --padding-left: calc(( 1280px - (840px - 2 * 44px) ) / 2 + (840px - 2 * 44px - 100%)); --padding-right: 54px; width: calc(100% + 210px); padding-left: calc(-100% + 1016px); padding-right: 54px; margin-left: calc(100% - 1016px); color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="ds-scroll-area__gutters" style="--dsl-scroll-area-scrollbar-bg: #e5e5e5; --dsl-scroll-area-scrollbar-hover: #d4d4d4; --dsl-scroll-area-horizontal-gutter-padding: 2px 0; --dsl-scroll-area-vertical-gutter-padding: 0 2px; pointer-events: none; z-index: 1000; transition: opacity 0.1s ease-out 1s; opacity: 1 !important; display: block; --container-height: 276px; position: sticky; top: 0px; left: 0px; right: 0px; width: 962px; height: 0px;"><div class="ds-scroll-area__horizontal-gutter" style="position: absolute; padding: 2px 0px; left: 0px; right: 0px; display: block; top: 262px; height: 10px;"></div><div class="ds-scroll-area__vertical-gutter" style="position: absolute; padding: 0px 2px; right: 0px; top: 8px; bottom: -268px; width: 10px;"></div></div>
Field | Type | Required | Range | Description
-- | -- | -- | -- | --
latitude | float | Yes | -90 to 90 | GPS latitude
longitude | float | Yes | -180 to 180 | GPS longitude
timestamp | string (ISO8601) | Yes | Valid datetime | Current time with timezone
crowd_density | float | No | 0 to 1 | Estimated crowd (default 0.5)
lighting_score | float | No | 0 to 1 | Street lighting (default 0.5)

</div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><em><span class="">Last updated: June 2026</span></em></p><!--EndFragment-->
</body>
</html>