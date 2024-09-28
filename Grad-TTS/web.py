from bs4 import BeautifulSoup

html = '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="shortcut icon" href="/favicon.ico">
  <link type="application/opensearchdescription+xml" rel="search" href="/OpensearchDescription.xml"/>

  <title>XT.COM Statistics: Markets, Trading Volume &amp; Trust Score | CoinGecko</title>
  <meta name="description" content="View XT.COM 24h trade volume, volume charts &amp; statistics, fee structure, market listings, trading pairs, and other cryptocurrency exchange info." />
  
  

  <!-- OptanonConsentNoticeStart -->
<script
  src="https://cdn-apac.onetrust.com/scripttemplates/otSDKStub.js"
  data-document-language="true"
  type="text/javascript"
  charset="UTF-8"
  defer
  data-domain-script="49e8a847-f2c7-4b58-a340-caf0924064fe"
></script>
<script type="text/javascript">
  const STRICT_COOKIE = "C0001";
  const PERF_COOKIE = "C0002";
  const FUNC_COOKIE = "C0003";
  const TARGET_COOKIE = "C0004";

  const YT_DOMAIN = "www.youtube.com";
  const TW_DOMAIN = "platform.twitter.com";
  const TW_CONTAINER = "twitter-tweet";

  const CONTENT_PLACEHOLDER = "content-placeholder";

  // TODO: confirm if i18n needed
  const contentPlaceholderTemplate = `
    <div class="tw-p-6 dark:tw-bg-moon-900">
      <div class="tw-flex tw-flex-col tw-gap-4">
        <div class="tw-p-6 tw-border-solid tw-border-2 tw-border-gray-200 tw-rounded-lg dark:tw-border-moon-800">
          <div class="tw-flex">
            <div class="tw-flex-shrink-0">
              <i class="tw-text-sm fas fa-exclamation-triangle tw-text-gray-700 dark:tw-text-moon-100"></i>
            </div>
            <div class="tw-ml-3">
              <div class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-base tw-leading-6 tw-flex-grow tw-mb-1">
                Couldn't load content
              </div>
              <div class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-base tw-leading-6 tw-flex-grow">
                This feature is currently not available because you need to provide consent to functional cookies.
                Please update your
                <span class="tw-cursor-pointer tw-font-semibold tw-underline tw-text-gray-700
                             hover:tw-text-primary-500 hover:tw-underline dark:tw-text-slate-50 dark:hover:tw-text-primary-400"
                      onclick="javascript:openPrefCenter();">Cookie Preferences</span>.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  function openPrefCenter() {
    if (window.OneTrust === undefined) { return; }

    OneTrust.ToggleInfoDisplay();
  }

  // Convenient function to extract consent values from OneTrust cookie,
  // returns an object containing category as key, true/false as value
  function getConsentCookies() {
    if (OnetrustActiveGroups === undefined) { return {}; }

    const categories = OnetrustActiveGroups.split(",").filter(c => c !== "");

    if (categories.length === 0) { return {}; }

    return categories.reduce(function (acc, cat) {
      acc[cat] = true;
      return acc;
    }, {});
  }

  // Convenient function to check if user opt-in the category,
  // pass the value from the cookie
  function optedIn(consent) {
    return !!consent;
  }

  // Convenient function to check if user opt-out the category,
  // pass the value from the cookie
  function optedOut(consent) {
    return !optedIn(consent);
  }

  // Convenient function to lookup elements by tag and
  // src/data-src domain
  function findEmbeddedElements(tag, domain) {
    const srcSelector = `${tag}[src*="${domain}"]`;
    const dataSrcSelector = `${tag}[data-src*="${domain}"]`;
    const selectors = `${srcSelector}, ${dataSrcSelector}`;
    return document.querySelectorAll(selectors);
  }

  // Convenient function to toggle between src and data-src attribute
  function toggleFrameSrc(ele, enabled) {
    const origSrc = ele.getAttribute("data-src") || ele.getAttribute("src");
    if (enabled) {
      ele.removeAttribute("data-src");
      ele.setAttribute("src", origSrc);
      ele.style.display = "block";
    } else {
      ele.removeAttribute("src");
      ele.setAttribute("data-src", origSrc);
      ele.style.display = "none";
    }
  }

  // Convenient function to toggle between script types
  function toggleScriptType(ele, enabled) {
    if (enabled) {
      ele.setAttribute("type", "text/javascript");
    } else {
      ele.setAttribute("type", "text/plain");
    }
  }

  // Convenient function to toggle between frame display and notice display
  function toggleTagDisplay(ele, enabled) {
    ele.style.height = "auto";

    if (enabled) {
      for (let div of ele.getElementsByClassName(CONTENT_PLACEHOLDER)) {
        div.remove();
      };
    } else {
      // Prevent appending more than one placeholder
      if (ele.querySelector(`.${CONTENT_PLACEHOLDER}`) !== null) { return; }

      const contentPlaceholder = document.createElement("div");
      contentPlaceholder.classList.add(CONTENT_PLACEHOLDER);
      contentPlaceholder.innerHTML = contentPlaceholderTemplate;
      ele.appendChild(contentPlaceholder);
    }
  }

  // Detect whether there're embedded Youtube videos,
  // and change to data-src if user opt-out of cookies.
  function toggleVideoCookies(enabled) {
    const vidFrames = findEmbeddedElements("iframe", YT_DOMAIN);

    for (let vidFrame of vidFrames) {
      toggleFrameSrc(vidFrame, enabled);
      const vidContainer = vidFrame.parentElement;
      toggleTagDisplay(vidContainer, enabled);
    }
  }

  // Detect whether there're embedded Twitter/X posts,
  // and change to data-src if user opt-out of cookies.
  function toggleTwitterCookies(enabled) {
    // Embedded Twitter posts
    const tweetFrames = findEmbeddedElements("iframe", TW_DOMAIN);

    for (let tweetFrame of tweetFrames) {
      toggleFrameSrc(tweetFrame, enabled);
      const tweetContainer = tweetFrame.parentElement;
      // Only post iframe has a container parent
      if (tweetContainer.classList.contains(TW_CONTAINER)) {
        toggleTagDisplay(tweetContainer, enabled);
      }
    }

    // Twitter JS script
    const tweetScript = findEmbeddedElements("script", TW_DOMAIN)[0];
    if (tweetScript !== undefined) {
      toggleScriptType(tweetScript, enabled);
    }
  }

  // remove all targeted ad local storage
  function removeTargetingAdLocalStorage(enabled) {
    if (!enabled) {
      localStorage.removeItem("adTargetingCoins");
      localStorage.removeItem("adTargetingCategories");
      localStorage.removeItem("adTargetingChains");
      localStorage.removeItem("adTargetingDeveloper");
    }
  }

  function sendPerformanceCookieChanged(enabled) {
    window.dispatchEvent(
      new CustomEvent("coingecko-performance-cookie-consent-changed", {
        detail: {
          enabled: enabled,
        }
      })
    );
  }
  
  // TODO:
  // Add more logic to this function to manually block/unblock sources that set cookie,
  // eg. embedded Youtube videos, BuySellAds banner
  function toggleCookies() {
    const categories = getConsentCookies();

    toggleVideoCookies(optedIn(categories[FUNC_COOKIE]));
    toggleTwitterCookies(optedIn(categories[FUNC_COOKIE]));
    removeTargetingAdLocalStorage(optedIn(categories[TARGET_COOKIE]));
  }

  // OneTrust callback after banner SDK is loaded
  function OptanonWrapper() {
    // On first load, hide the consent banner until user scrolls,
    // subsequently do not trigger show on scroll
    if (!OneTrust.IsAlertBoxClosed()) {
      document.getElementById("onetrust-consent-sdk").style.display = "none";

      window.addEventListener("scroll", function() {
        document.getElementById("onetrust-consent-sdk").style.display = "block";
      });
    }

    document.getElementById("ot-sdk-btn").addEventListener("click", openPrefCenter);

    // On first load, always refresh consent changes accordingly
    toggleCookies();

    // OneTrust callback when user consent changes
    OneTrust.OnConsentChanged(function() {
      toggleCookies();
      sendPerformanceCookieChanged(optedIn(getConsentCookies()[PERF_COOKIE]));
    });
  }
</script>
<!-- OptanonConsentNoticeEnd -->


  <!-- START: Third-Party JS -->
  <script type="text/plain" class="optanon-category-C0002">(function (w, d, s, l, i) {
      w[l] = w[l] || [];
      w[l].push({
          'gtm.start':
              new Date().getTime(), event: 'gtm.js'
      });
      var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
      j.async = true;
      j.src =
          'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
      f.parentNode.insertBefore(j, f);
  })(window, document, 'script', 'dataLayer', 'GTM-NP34MX7');</script>
  <!-- END: Third-Party JS -->

  <!-- START: Preload Resources -->
  <link rel="preload" fetchpriority="high" as="image" href="https://static.coingecko.com/s/coingecko-logo-8903d34ce19ca4be1c81f0db30e924154750d208683fad7ae6f2ce06c76d0a56.png"/>

  <link rel="preconnect" href="//www.googletagmanager.com"/>
  <link rel="preconnect" href="https://static.coingecko.com" crossorigin="anonymous"/>
  <link rel="dns-prefetch" href="https://static.coingecko.com" crossorigin="anonymous"/>
    <script type="text/javascript" defer src="https://ads.coingecko.com/ascendeum/pub/asc.coingecko.js"></script>
    <script>
  window.googletag = window.googletag || { cmd: [] };
  const coins = JSON.parse(localStorage.getItem("adTargetingCoins"));
  const categories = JSON.parse(localStorage.getItem("adTargetingCategories"));
  const chains = JSON.parse(localStorage.getItem("adTargetingChains"));
  const developer = JSON.parse(localStorage.getItem("adTargetingDeveloper"));

  googletag.cmd.push(() => {
    googletag.pubads().setTargeting("kevelcoin", coins)
      .setTargeting("kevelchain", chains)
      .setTargeting("kevelcategories", categories)
      .setTargeting("keveldeveloper", developer);
    });
</script>

  <!-- END: Preload Resources -->

  <!-- START: SEO Tags -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="XT.COM Statistics: Markets, Trading Volume &amp; Trust Score | CoinGecko" />
  <meta property="og:description" content="View XT.COM 24h trade volume, volume charts &amp; statistics, fee structure, market listings, trading pairs, and other cryptocurrency exchange info." />
  <meta property="og:image" content="https://assets.coingecko.com/markets/images/404/large/20240701-155217.jpeg?1719895821" />
  <meta property="og:url" content="https://www.coingecko.com/en/exchanges/xt" />
  <meta property="og:site_name" content="CoinGecko" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@coingecko" />
  <meta name="twitter:creator" content="@coingecko" />
  <meta name="twitter:title" content="XT.COM Statistics: Markets, Trading Volume &amp; Trust Score | CoinGecko" />
  <meta name="twitter:description" content="View XT.COM 24h trade volume, volume charts &amp; statistics, fee structure, market listings, trading pairs, and other cryptocurrency exchange info." />
  <meta name="twitter:image" content="https://assets.coingecko.com/markets/images/404/large/20240701-155217.jpeg?1719895821" />

  <link rel="canonical" href="https://www.coingecko.com/en/exchanges/xt" />
<link rel="alternate" hreflang="en" href="https://www.coingecko.com/en/exchanges/xt" /><link rel="alternate" hreflang="zh" href="https://www.coingecko.com/zh/exchanges/xt" /><link rel="alternate" hreflang="zh-tw" href="https://www.coingecko.com/zh-tw/%E4%BA%A4%E6%98%93%E5%B9%B3%E5%8F%B0/xt" /><link rel="alternate" hreflang="de" href="https://www.coingecko.com/de/b%C3%B6rsen/xt" /><link rel="alternate" hreflang="fr" href="https://www.coingecko.com/fr/platesformes/xt" /><link rel="alternate" hreflang="es" href="https://www.coingecko.com/es/intercambios/xt" /><link rel="alternate" hreflang="ja" href="https://www.coingecko.com/ja/%E4%BA%A4%E6%8F%9B%E6%89%80/xt" /><link rel="alternate" hreflang="id" href="https://www.coingecko.com/id/pertukaran/xt" /><link rel="alternate" hreflang="ru" href="https://www.coingecko.com/ru/%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD/xt" /><link rel="alternate" hreflang="ko" href="https://www.coingecko.com/ko/%EA%B1%B0%EB%9E%98%EC%86%8C/xt" /><link rel="alternate" hreflang="ar" href="https://www.coingecko.com/ar/%D8%B9%D9%85%D9%84%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D8%AA%D8%A8%D8%A7%D8%AF%D9%84/xt" /><link rel="alternate" hreflang="th" href="https://www.coingecko.com/th/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%82%E0%B8%B2%E0%B8%A2/xt" /><link rel="alternate" hreflang="vi" href="https://www.coingecko.com/vi/san_giao_dich/xt" /><link rel="alternate" hreflang="it" href="https://www.coingecko.com/it/cambi/xt" /><link rel="alternate" hreflang="pt" href="https://www.coingecko.com/pt/c%C3%A2mbios/xt" /><link rel="alternate" hreflang="pl" href="https://www.coingecko.com/pl/gie%C5%82dy/xt" /><link rel="alternate" hreflang="tr" href="https://www.coingecko.com/tr/borsalar/xt" /><link rel="alternate" hreflang="hu" href="https://www.coingecko.com/hu/exchanges/xt" /><link rel="alternate" hreflang="nl" href="https://www.coingecko.com/nl/exchanges/xt" /><link rel="alternate" hreflang="ro" href="https://www.coingecko.com/ro/exchanges/xt" /><link rel="alternate" hreflang="sv" href="https://www.coingecko.com/sv/exchanges/xt" /><link rel="alternate" hreflang="cs" href="https://www.coingecko.com/cs/exchanges/xt" /><link rel="alternate" hreflang="da" href="https://www.coingecko.com/da/exchanges/xt" /><link rel="alternate" hreflang="el" href="https://www.coingecko.com/el/exchanges/xt" /><link rel="alternate" hreflang="hi" href="https://www.coingecko.com/hi/exchanges/xt" /><link rel="alternate" hreflang="no" href="https://www.coingecko.com/no/exchanges/xt" /><link rel="alternate" hreflang="sk" href="https://www.coingecko.com/sk/exchanges/xt" /><link rel="alternate" hreflang="uk" href="https://www.coingecko.com/uk/exchanges/xt" /><link rel="alternate" hreflang="he" href="https://www.coingecko.com/he/exchanges/xt" /><link rel="alternate" hreflang="fi" href="https://www.coingecko.com/fi/exchanges/xt" /><link rel="alternate" hreflang="bg" href="https://www.coingecko.com/bg/exchanges/xt" /><link rel="alternate" hreflang="hr" href="https://www.coingecko.com/hr/exchanges/xt" /><link rel="alternate" hreflang="lt" href="https://www.coingecko.com/lt/exchanges/xt" /><link rel="alternate" hreflang="sl" href="https://www.coingecko.com/sl/exchanges/xt" />  <!-- END: SEO Tags -->

  <!-- START: Stylesheets -->
  <link rel="stylesheet" href="https://static.coingecko.com/packs/css/v2/application-f034dd68.chunk.css" />
  <link rel="preload" href="https://static.coingecko.com/s/fonts-bfbedf42bf4ac98d260fc87ae2b5dda0d92c632e80f03d70be2b06afd4e4f4d4.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://static.coingecko.com/s/fonts-bfbedf42bf4ac98d260fc87ae2b5dda0d92c632e80f03d70be2b06afd4e4f4d4.css"></noscript>
  <!-- END: Stylesheets -->

  <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96"/>
  <link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32"/>
  <link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16"/>
  <meta name="application-name" content="CoinGecko"/>
  <meta name="action-cable-url" content="wss://cables.coingecko.com/cable" />

  

  <!-- START: Other JS Scripts -->
  <script type="text/plain" class="optanon-category-C0002" async src="https://www.googletagmanager.com/gtag/js?id=G-LJR3232ZPB"></script>
  <script type="text/plain" class="optanon-category-C0002">
      window.dataLayer = window.dataLayer || [];

      function gtag() {
          dataLayer.push(arguments);
      }

      gtag('js', new Date());
      gtag('config', 'G-LJR3232ZPB');
  </script>
  <script type="text/javascript" async src="https://btloader.com/tag?o=5172243878903808&upapi=true"></script>
  <!-- END: Other JS Scripts -->
</head>

<body data-controller="tooltips settings login-state csrf-meta auth currency price percent-change async-percent-change application ads index-trending-coins add-coin-id-to-cookies add-nft-contract-id-to-cookies generate-uuid mixpanel-init analytics-tracker"
      data-currency-symbols="{&quot;btc&quot;:&quot;BTC&quot;,&quot;eth&quot;:&quot;ETH&quot;,&quot;ltc&quot;:&quot;LTC&quot;,&quot;bch&quot;:&quot;BCH&quot;,&quot;bnb&quot;:&quot;BNB&quot;,&quot;eos&quot;:&quot;EOS&quot;,&quot;xrp&quot;:&quot;XRP&quot;,&quot;xlm&quot;:&quot;XLM&quot;,&quot;link&quot;:&quot;LINK&quot;,&quot;dot&quot;:&quot;DOT&quot;,&quot;yfi&quot;:&quot;YFI&quot;,&quot;usd&quot;:&quot;$&quot;,&quot;aed&quot;:&quot;DH&quot;,&quot;ars&quot;:&quot;$&quot;,&quot;aud&quot;:&quot;A$&quot;,&quot;bdt&quot;:&quot;৳&quot;,&quot;bhd&quot;:&quot;BD&quot;,&quot;bmd&quot;:&quot;$&quot;,&quot;brl&quot;:&quot;R$&quot;,&quot;cad&quot;:&quot;CA$&quot;,&quot;chf&quot;:&quot;Fr.&quot;,&quot;clp&quot;:&quot;CLP$&quot;,&quot;cny&quot;:&quot;¥&quot;,&quot;czk&quot;:&quot;Kč&quot;,&quot;dkk&quot;:&quot;kr.&quot;,&quot;eur&quot;:&quot;€&quot;,&quot;gbp&quot;:&quot;£&quot;,&quot;gel&quot;:&quot;₾&quot;,&quot;hkd&quot;:&quot;HK$&quot;,&quot;huf&quot;:&quot;Ft&quot;,&quot;idr&quot;:&quot;Rp&quot;,&quot;ils&quot;:&quot;₪&quot;,&quot;inr&quot;:&quot;₹&quot;,&quot;jpy&quot;:&quot;¥&quot;,&quot;krw&quot;:&quot;₩&quot;,&quot;kwd&quot;:&quot;KD&quot;,&quot;lkr&quot;:&quot;Rs&quot;,&quot;mmk&quot;:&quot;K&quot;,&quot;mxn&quot;:&quot;MX$&quot;,&quot;myr&quot;:&quot;RM&quot;,&quot;ngn&quot;:&quot;₦&quot;,&quot;nok&quot;:&quot;kr&quot;,&quot;nzd&quot;:&quot;NZ$&quot;,&quot;php&quot;:&quot;₱&quot;,&quot;pkr&quot;:&quot;₨&quot;,&quot;pln&quot;:&quot;zł&quot;,&quot;rub&quot;:&quot;₽&quot;,&quot;sar&quot;:&quot;SR&quot;,&quot;sek&quot;:&quot;kr&quot;,&quot;sgd&quot;:&quot;S$&quot;,&quot;thb&quot;:&quot;฿&quot;,&quot;try&quot;:&quot;₺&quot;,&quot;twd&quot;:&quot;NT$&quot;,&quot;uah&quot;:&quot;₴&quot;,&quot;vef&quot;:&quot;Bs.F&quot;,&quot;vnd&quot;:&quot;₫&quot;,&quot;zar&quot;:&quot;R&quot;,&quot;xdr&quot;:&quot;XDR&quot;,&quot;xag&quot;:&quot;XAG&quot;,&quot;xau&quot;:&quot;XAU&quot;,&quot;bits&quot;:&quot;μBTC&quot;,&quot;sats&quot;:&quot;sats&quot;}"
      data-currency-override=""
      data-exchange-rate-json="{&quot;usd&quot;:&quot;65711.301&quot;,&quot;gbp&quot;:&quot;48971.281&quot;,&quot;eur&quot;:&quot;58810.76&quot;,&quot;cny&quot;:&quot;460708.506&quot;,&quot;jpy&quot;:&quot;9507516.324&quot;,&quot;cad&quot;:&quot;88542.364&quot;,&quot;rub&quot;:&quot;6085851.139&quot;,&quot;hkd&quot;:&quot;511152.509&quot;,&quot;sek&quot;:&quot;665040.755&quot;,&quot;sgd&quot;:&quot;84324.816&quot;,&quot;krw&quot;:&quot;86568126.128&quot;,&quot;aud&quot;:&quot;95343.024&quot;,&quot;zar&quot;:&quot;1128496.322&quot;,&quot;inr&quot;:&quot;5495308.075&quot;,&quot;myr&quot;:&quot;272373.344&quot;,&quot;idr&quot;:&quot;991941931.839&quot;,&quot;brl&quot;:&quot;357508.907&quot;,&quot;nzd&quot;:&quot;103910.266&quot;,&quot;mxn&quot;:&quot;1291194.153&quot;,&quot;php&quot;:&quot;3672111.807&quot;,&quot;dkk&quot;:&quot;438557.226&quot;,&quot;pln&quot;:&quot;251562.969&quot;,&quot;xau&quot;:&quot;24.5996828394816&quot;,&quot;xag&quot;:&quot;2047.62329573886&quot;,&quot;twd&quot;:&quot;2085808.067&quot;,&quot;xdr&quot;:&quot;48620.909&quot;,&quot;chf&quot;:&quot;55616.731&quot;,&quot;eth&quot;:&quot;24.6452405015994&quot;,&quot;aed&quot;:&quot;241357.61&quot;,&quot;ars&quot;:&quot;63590975.246&quot;,&quot;kwd&quot;:&quot;20054.234&quot;,&quot;lkr&quot;:&quot;19699358.072&quot;,&quot;sar&quot;:&quot;246485.786&quot;,&quot;try&quot;:&quot;2244507.365&quot;,&quot;thb&quot;:&quot;2130721.807&quot;,&quot;pkr&quot;:&quot;18250325.635&quot;,&quot;nok&quot;:&quot;692333.615&quot;,&quot;ils&quot;:&quot;242478.316&quot;,&quot;huf&quot;:&quot;23309769.99&quot;,&quot;czk&quot;:&quot;1478372.861&quot;,&quot;clp&quot;:&quot;59479241.689&quot;,&quot;bdt&quot;:&quot;7853257.658&quot;,&quot;bhd&quot;:&quot;24763.895&quot;,&quot;bmd&quot;:&quot;65711.301&quot;,&quot;mmk&quot;:&quot;137862310.602&quot;,&quot;vef&quot;:&quot;6579.672&quot;,&quot;bch&quot;:&quot;184.207838957812&quot;,&quot;ltc&quot;:&quot;960.265078661436&quot;,&quot;eos&quot;:&quot;120653.333426718&quot;,&quot;bnb&quot;:&quot;107.831995948817&quot;,&quot;xlm&quot;:&quot;665387.607917633&quot;,&quot;xrp&quot;:&quot;110230.698326062&quot;,&quot;vnd&quot;:&quot;1618106807.766&quot;,&quot;uah&quot;:&quot;2705623.61&quot;,&quot;byn&quot;:&quot;215040.957069972&quot;,&quot;link&quot;:&quot;5160.30441180667&quot;,&quot;dot&quot;:&quot;13496.1268468127&quot;,&quot;yfi&quot;:&quot;12.2804030682843&quot;,&quot;ngn&quot;:&quot;109105730.828&quot;,&quot;bits&quot;:&quot;1000000.0&quot;,&quot;sats&quot;:&quot;100000000.0&quot;,&quot;gel&quot;:&quot;179063.296&quot;}"

      data-locale="en"
      data-controller-name="exchanges"
      data-action-name="show"
      data-category-key=""
      data-coin-name=""

      data-kevel-api-proxy-endpoint="https://geckad.com/kevel/ad"
      data-mixpanel-token="baf3ceb56b3378245580f49a03fc37e3"
      data-mixpanel-proxy-url="https://mixpanel-proxy.coingecko.com"
>

<!-- Google Tag Manager (noscript) -->
<noscript>
  <iframe
      data-src="https://www.googletagmanager.com/ns.html?id=GTM-NP34MX7"
      height="0" width="0" style="display:none;visibility:hidden"
      class="optanon-category-C0002">
  </iframe>
</noscript>
<!-- End Google Tag Manager (noscript) -->


<header class="header dashboard tw-flex tw-flex-col">
  <!-- Top announcements -->
    <div id="announcement" class="tw-bg-gray-800 dark:tw-bg-moon-800" style="display: none;">
        <div class="container tw-flex tw-justify-between tw-items-center tw-py-2 tw-px-4 gecko-override-links-primary">
          <div data-view-component="true" class="tw-text-gray-50 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
            ⏰ GeckoCon 2024: <a href="https://bit.ly/3yBUkqc" target="_blank" rel="noopener"><b>Last Chance For 25% Off</b></a>

</div>          <i data-action="click-&gt;application#hideAnnouncement" data-view-component="true" class="fas fa-fw fa-times tw-cursor-pointer tw-text-gray-50 dark:tw-text-moon-50"></i>

        </div>
    </div>

  <!-- Preflight script that MUST run before HTML parsing continues -->
  <script>
    function hasCookie(cookie) {
      return !!document.cookie.split(';').filter(function (item) {
          return item.indexOf(cookie) >= 0
      }).length
    }

    // Apply dark mode immediately to prevent flicker.
    if (hasCookie("is_dark=true")) {
      document.body.classList.add("darktheme");
      document.body.classList.add("tw-dark");
    }

    // Prevent header announcement from showing if closed previously.
    if (!hasCookie("top_announcement_header_disabled=1")) {
      document.getElementById("announcement").style.display = "block";
    }
  </script>

  <!-- Navbar -->
  

<div class="tw-grid" data-controller="navbar" data-action="navbar:click:outside->navbar#hideAccountMenu">
  <!-- Overall Stats -->
  <div class="container tw-order-2 2lg:tw-order-none tw-overflow-x-auto 2lg:tw-py-2.5">
    <div class="tw-py-2 tw-flex tw-items-center">
      <div class="tw-flex-1 tw-flex tw-gap-x-4 tw-whitespace-nowrap tw-pr-[15px] 2lg:tw-pr-0">
        <div data-view-component="true" class="tw-hidden 2lg:tw-block tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
          Coins:
          <a href="/" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  14,678</a>

</div>
        <div data-view-component="true" class="tw-hidden 2lg:tw-block tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
          Exchanges:
          <a href="/en/exchanges" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  1,199</a>

</div>
        <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
          Market Cap:
          <a href="/en/global-charts" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  
            <span class="no-wrap" data-price-btc="36707137.842719644" data-price-target="price" data-abbreviated="true">
              $2.399T
</span></a>          <span class="gecko-up"><i class="fas fa-fw fa-caret-up"></i>1.5%</span>

</div>
        <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
          24h Vol:
          <a href="/en/global-charts" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  
            <span class="no-wrap" data-price-btc="1604778.0506813636" data-price-target="price" data-abbreviated="true">
              $104.887B
</span></a>
</div>
        <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
          Dominance:
          <div class="tw-inline-flex tw-gap-x-2">
              <a href="/en/global-charts" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  
                BTC
                53.8%
</a>              <a href="/en/global-charts" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  
                ETH
                13.3%
</a>          </div>

</div>
        <div class="tw-flex tw-flex-col" x-data="{ navbar_gas: false }" @mouseover.away="navbar_gas = false">
          <div @mouseover="navbar_gas = true" @click="navbar_gas = true" data-view-component="true" class="tw-cursor-pointer tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
            <i data-view-component="true" class="fab fa-ethereum"></i>

            Gas:
            <span class="tw-font-semibold tw-text-slate-700 dark:tw-text-moon-50">
              46.350923393 GWEI
            </span>

</div>
          <div menu_position="bottom" data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]" x-data="popperable(&#39;navbar_gas&#39;)" data-placement="bottom" x-cloak="true">
  <div @click.away="navbar_gas = false" x-show="navbar_gas" x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" style="; display: none" data-view-component="true" class="!tw-w-44 dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <div @mouseover="navbar_gas = true" @click="navbar_gas = true" data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  
                <div class='tw-flex tw-justify-between'>
                  Fast: <span class="tw-font-semibold">48.3761319 GWEI</span>
                </div>
                <div class='tw-flex tw-justify-between'>
                  Standard: <span class="tw-font-semibold">46.350923393 GWEI</span>
                </div>
                <div class='tw-flex tw-justify-between'>
                  Safe: <span class="tw-font-semibold">45.6381129 GWEI</span>
                </div>

</div>              <div data-view-component="true" class="tw-mt-1 tw-opacity-70 dark:tw-opacity-50 tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  Data by Etherscan
</div>

</div>

</div></div></div>        </div>
      </div>

      <div class="tw-hidden 2lg:tw-block tw-justify-end tw-items-center 2lg:-tw-my-2.5 tw-pr-4" data-login-state-target="placeholder">
        <i data-view-component="true" class="fas fa-spin fa-spinner-third fa-fw tw-text-gray-900 dark:tw-text-moon-200"></i>

      </div>
      <div class="tw-hidden 2lg:tw-flex tw-justify-end tw-items-center tw-gap-x-2 2lg:-tw-my-2.5 !tw-hidden" data-login-state-target="transition">
        <div x-data="{open: false}" menu_position="right" data-view-component="true" class="tw-inline-block tw-text-left">
  <div @click="open = !open">
    <button :class="open &amp;&amp; &#39;gecko-button-dropdown-secondary gecko-button-dropdown-open&#39;" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      <i data-view-component="true" class="far fa-gear fa-fw"></i>


</div></button>
  </div>

  <div class="tw-z-[2000]" x-data="popperable(&#39;open&#39;)" data-placement="bottom-end" x-cloak="true">
  <div @click.away="open = false" x-show="open" x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" style="; display: none" data-view-component="true" class="dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true">
  
              <div @click="Modal.show(&#39;language_selector&#39;); open = false;" data-view-component="true" class="tw-cursor-pointer tw-flex tw-justify-between dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              Language
              <div data-view-component="true" class="tw-text-gray-500 dark:text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  English
</div>

  
</div>            <div @click="Modal.show(&#39;currency_selector&#39;); open = false;" data-view-component="true" class="tw-cursor-pointer tw-flex tw-justify-between dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              Currency
              <div data-settings-target="currencyText" data-view-component="true" class="tw-text-gray-500 dark:text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  USD
</div>

  
</div>            <div data-action="click-&gt;settings#toggleDarkMode" data-view-component="true" class="tw-cursor-pointer tw-flex tw-justify-between dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              Dark Mode
              <label data-view-component="true" class="tw-pointer-events-none tw-relative tw-inline-flex tw-items-center tw-cursor-pointer">
  <input data-settings-target = darkModeToggle id="" unchecked type="checkbox" class="tw-sr-only tw-peer">
  <div class="after:tw-content-[&#39;&#39;] tw-w-11 tw-h-4 tw-bg-gray-200 tw-rounded-md dark:tw-bg-gray-700 after:tw-absolute after:tw-top-[-4px] after:tw-left-[0px] after:tw-drop-shadow after:tw-bg-no-repeat after:tw-bg-white after:tw-bg-center after:tw-bg-[url(&#39;icons/cross.svg&#39;)] after:tw-align-middle after:tw-border-2 after:tw-rounded-lg after:tw-h-6 after:tw-w-6 after:tw-transition-all after:tw-border-gray-200 dark:tw-border-gray-600 after:dark:tw-border-moon-600 after:dark:tw-bg-moon-50after:dark:tw-bg-[url(&#39;icons/cross_dark.svg&#39;)] peer-checked:tw-bg-primary-500 peer-checked:after:tw-border-primary-500 peer-checked:after:tw-bg-[url(&#39;icons/tick.svg&#39;)] peer-checked:after:dark:tw-bg-moon-50 peer-checked:after:tw-translate-x-full"></div>
</label>

  
</div>
</div>

</div></div></div>
        <div x-data="{open: false}" menu_position="right" data-login-state-target="loggedInItem" data-view-component="true" class="tw-inline-block tw-text-left">
  <div @click="open = !open">
    <button :class="open &amp;&amp; &#39;gecko-button-dropdown-secondary gecko-button-dropdown-open&#39;" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      <i data-view-component="true" class="far fa-user fa-fw"></i>


</div></button>
  </div>

  <div class="tw-z-[2000]" x-data="popperable(&#39;open&#39;)" data-placement="bottom-end" x-cloak="true">
  <div @click.away="open = false" x-show="open" x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" style="; display: none" data-view-component="true" class="dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">My Account</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/account/security" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Login and Security
  
</span>
            <span data-action="click-&gt;application#navigateToUrl" data-url="/en/premium/pricing" data-login-state-target="subscribeButton" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Upgrade to Premium
  
</span>
            <span data-action="click-&gt;application#navigateToUrl" data-url="/account/subscriptions" data-login-state-target="premiumItem" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Manage Subscription
  
</span>
            <span data-action="click-&gt;application#navigateToUrl" data-url="/account/premium-newsletter?locale=en" data-login-state-target="premiumItem" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Premium Newsletter
  
</span>

</div>
      <div data-login-state-target="developerGroup" data-view-component="true" class="tw-hidden">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">For Developers</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/en/developers/dashboard" data-login-state-target="developerGroup" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Developer&#39;s Dashboard
  
</span>

</div>
      <div data-login-state-target="authorshipGroup" data-view-component="true" class="tw-hidden">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">For Authors</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/buzz/new?locale=en" data-login-state-target="authorshipGroup" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Create New Post
  
</span>
            <span data-action="click-&gt;application#navigateToUrl" data-url="/buzz/dashboard?locale=en" data-login-state-target="authorshipGroup" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Buzz Dashboard
  
</span>

</div>
      <div data-view-component="true">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
              <span data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;application#navigateToUrl" data-analytics-event="select_sign_out_cta" data-url="/account/sign_out?locale=en" data-method="delete" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Sign Out
  
</span>

</div>

</div></div></div>        <a href="/en/premium/pricing" data-login-state-target="subscribeButton" role="button" data-view-component="true" class="tw-hidden tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold">
  
      Go Ad-free

</div></a>

        <button data-login-state-target="loggedOutItem" data-action="click-&gt;auth#openSignInModal" data-analytics-origin="navbar_login" type="button" data-view-component="true" class="tw-hidden tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      Login

</div></button>
        <button data-login-state-target="loggedOutItem" data-action="click-&gt;auth#openSignUpModal" data-analytics-origin="navbar_sign_up" type="button" data-view-component="true" class="tw-hidden tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold">
  
      Sign up

</div></button>
      </div>
    </div>
  </div>
  <div data-view-component="true" class="tw-order-2 2lg:tw-order-none tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>


  <!-- Menu Items -->
  <div class="tw-relative">
    <div class="container 2lg:tw-py-3 tw-flex tw-flex-col 2lg:tw-flex-row">
      <div class="tw-flex tw-gap-x-4 tw-items-center tw-pt-4 2lg:tw-pt-0 tw-z-[1120]">
        <!-- Mobile Nav Menu Toggle -->
        <i data-action="click-&gt;navbar#toggleMenu" data-view-component="true" class="tw-text-base tw-cursor-pointer tw-py-2 tw-pr-2 2lg:!tw-hidden far fa-fw fa-bars tw-text-gray-700 dark:tw-text-moon-50"></i>


        <!-- Logo -->
        <!-- Note: When updating logo, make sure to update the preload tag in layouts/application.html.erb accordingly -->
        <a class="tw-inline-block" href="/">
          <img alt="CoinGecko" class="!tw-h-8 2lg:!tw-h-10 tw-block dark:tw-hidden" src="https://static.coingecko.com/s/coingecko-logo-8903d34ce19ca4be1c81f0db30e924154750d208683fad7ae6f2ce06c76d0a56.png" />
          <img alt="CoinGecko" class="!tw-h-8 2lg:!tw-h-10 tw-hidden dark:tw-block" src="https://static.coingecko.com/s/coingecko-logo-white-ea42ded10e4d106e14227d48ea6140dc32214230aa82ef63d0499f9c1e109656.png" />
</a>
        <!-- Mobile App Link -->
        <a class="tw-ml-auto lg:tw-hidden" href="https://coingecko.app.link/lTInCXLGz4">
          <button type="button" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold">
  
      Use App

</div></button>
</a>
        <!-- Get Mobile App Modal -->
        <button onclick="Modal.show(&#39;get_app_modal&#39;)" type="button" data-view-component="true" class="tw-ml-auto tw-hidden lg:tw-inline 2lg:tw-hidden tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold">
  
      
          <i data-view-component="true" class="fas fa-qrcode"></i>

          Get App


</div></button>      </div>

      <div class="nav-backdrop tw-hidden"></div>
      <div class="nav-wrapper container 2lg:!tw-px-0 tw-hidden 2lg:tw-flex 2lg:tw-mr-4">
        <!-- Cryptocurrencies -->
        <div class="tw-flex tw-flex-col 2lg:tw-relative 2lg:tw-mx-8" data-action="mouseover->navbar#handleOver mouseout->navbar#handleAway click->navbar#handleClick">
          <div class="tw-flex tw-items-center tw-cursor-pointer">
            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Cryptocurrencies
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-view-component="true" class="nav-items 2lg:tw-hidden dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-4 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <a href="/" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-ranking-star fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                By Market Cap

  
</a>              <a href="/en/categories" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-shapes fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Categories

  
</a>              <a href="/en/chains" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-link fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Chains

  
</a>
</div>
      <div data-view-component="true">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">Popular</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
                <a href="/en/highlights" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-list-ol fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Highlights

  
</a>              <a href="/en/new-cryptocurrencies" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-sparkles fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                New Cryptocurrencies

  
</a>              <a href="/en/crypto-gainers-losers" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-trophy-star fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Gainers &amp; Losers

  
</a>
</div>
      <div data-view-component="true">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">Tools</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
                <a href="/en/all-cryptocurrencies" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  All Coins
  
</a>
              <a href="/en/compare-cryptocurrencies" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Compare Coins
  
</a>
              <a href="/en/converter" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Converter
  
</a>
              <a href="/en/global-charts" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Global Chart
  
</a>

              <div data-view-component="true" class="tw-mt-2 2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

</div>

</div></div></div>        </div>


        <!-- Exchanges -->
        <div class="tw-flex tw-flex-col 2lg:tw-relative 2lg:tw-mr-8" data-action="mouseover->navbar#handleOver mouseout->navbar#handleAway click->navbar#handleClick">
          <div class="tw-flex tw-items-center tw-cursor-pointer">
            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Exchanges
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-view-component="true" class="nav-items 2lg:tw-hidden dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-4 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <a href="/en/exchanges" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-building-columns fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Crypto Exchanges

  
</a>              <a href="/en/exchanges/decentralized" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-cubes fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Decentralized Exchanges

  
</a>              <a href="/en/exchanges/derivatives" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-chart-line fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Derivatives

  
</a>
              <div data-view-component="true" class="tw-mt-2 2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

</div>

</div></div></div>        </div>


        <!-- NFT -->
        <div class="tw-flex tw-flex-col 2lg:tw-relative 2lg:tw-mr-8" data-action="mouseover->navbar#handleOver mouseout->navbar#handleAway click->navbar#handleClick">
          <div class="tw-flex tw-items-center tw-cursor-pointer">
            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  NFT
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-view-component="true" class="nav-items 2lg:tw-hidden dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-4 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <a href="/en/nft" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-image fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                NFT Floor Price

  
</a>              <a href="/en/categories/non-fungible-tokens-nft" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-hexagon-image fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                NFT Related Coins

  
</a>              <a href="/en/nft-portfolio" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-star fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                NFT Watchlist

  
</a>              <a href="/en/nft/global-stats" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-globe fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                NFT Global Chart

  
</a>
              <div data-view-component="true" class="tw-mt-2 2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

</div>

</div></div></div>        </div>


        <!-- Learn -->
        <div class="tw-flex tw-flex-col 2lg:tw-relative 2lg:tw-mr-8" data-action="mouseover->navbar#handleOver mouseout->navbar#handleAway click->navbar#handleClick">
          <div class="tw-flex tw-items-center tw-cursor-pointer">
            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Learn
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-view-component="true" class="nav-items 2lg:tw-hidden dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-4 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <a href="/learn" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-book-open-cover fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Learn Crypto

  
</a>              <a href="/research" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-lightbulb-on fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Research Insights

  
</a>              <a href="/en/news" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-newspaper fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                News

  
</a>              <a href="/en/publications/reports" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-chart-user fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Reports

  
</a>              <a href="https://landing.coingecko.com/earn/" target="_blank" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-graduation-cap fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Learn &amp; Earn

  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-arrow-up-right-from-square fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

</a>              <a href="https://www.youtube.com/@CoinGecko?sub_confirmation=1" target="_blank" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fab fa-youtube fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Videos

  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-arrow-up-right-from-square fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

</a>              <a href="https://newsletter.coingecko.com/landing/subscribe" target="_blank" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-envelope fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Newsletter

  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-arrow-up-right-from-square fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

</a>              <a href="/en/glossary" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-arrow-down-a-z fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Glossary

  
</a>
              <div data-view-component="true" class="tw-mt-2 2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

</div>

</div></div></div>        </div>


        <!-- Products -->
        <div class="tw-flex tw-flex-col 2lg:tw-relative 2lg:tw-mr-8" data-action="mouseover->navbar#handleOver mouseout->navbar#handleAway click->navbar#handleClick">
          <div class="tw-flex tw-items-center tw-cursor-pointer">
            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Products
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-view-component="true" class="nav-items 2lg:tw-hidden dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-4 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <a href="/en/portfolio" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-star fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                Crypto Portfolio

  
</a>              <a href="/en/mobile" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-mobile-screen-button fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                CoinGecko App

  
</a>              <a href="/en/premium/pricing" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  <i data-view-component="true" class="tw-mr-2 fas fa-crown fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

  
                CoinGecko Premium

  
</a>
</div>
      <div data-view-component="true">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">For Developers</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
                <a href="/en/api" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Crypto API
  
</a>
              <a href="/en/widgets" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Crypto Widget
  
</a>

</div>
      <div data-view-component="true">
  <div data-view-component="true" class="tw-p-2 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-xs">
  
  <span class="tw-shrink-0 tw-basis-auto">On-Chain</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
                <a href="https://www.geckoterminal.com?utm_source=coingecko&amp;utm_medium=referral&amp;utm_campaign=desktop_navigation" target="_blank" rel="noopener" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                GeckoTerminal

  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-arrow-up-right-from-square fa-fw tw-text-gray-400 dark:tw-text-moon-500"></i>

</a>
              <div data-view-component="true" class="tw-mt-2 2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

</div>

</div></div></div>        </div>


        <!-- Candy -->
        <div class="tw-flex tw-flex-col 2lg:tw-flex-row 2lg:tw-flex-1 tw-justify-end">
          <a class="tw-no-underline tw-flex tw-items-center tw-py-4 2lg:tw-py-0 2lg:tw-gap-x-1" data-login-state-target="candyItem" data-url="/en/candy" href="/en/candy">
            <div class="fa-fw tw-mr-2 2lg:tw-mr-0 tw-px-0.5">
              <img loading="lazy" height="20" width="13" alt="Candy Jar" class="tw-align-middle" src="https://static.coingecko.com/s/candy_notification-62af2d17629b138154e3fac22a492b51d914d18461f9283ae4bd5ad5730d8763.svg" />
            </div>
            <div data-view-component="true" class="tw-hidden 2lg:tw-block dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Candy
</div>
            <div data-view-component="true" class="tw-block 2lg:tw-hidden dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  My Candies
</div>
</a>          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
        </div>


        <!-- Portfolio -->
        <div class="tw-flex tw-flex-col 2lg:tw-relative 2lg:tw-ml-4" data-action="click->navbar#handleClick" data-login-state-target="portfolioItem">
          <div class="tw-flex tw-items-center 2lg:tw-cursor-pointer tw-no-underline">
            <i data-view-component="true" class="fas fa-fw fa-star tw-mr-2 2lg:tw-mr-0.5 tw-text-yellow-500"></i>

            <a class="nav-label tw-no-underline tw-hidden 2lg:tw-block" href="/en/portfolio">
              <div data-view-component="true" class="dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Portfolio
</div>
</a>            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-block 2lg:tw-hidden tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  My Portfolio
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-login-state-target="portfolioMenu" data-view-component="true" class="nav-items 2lg:tw-hidden 2lg:!tw-left-[unset] 2lg:!tw-right-0 2lg:tw-max-h-[28rem] 2lg:tw-overflow-y-auto dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true" class="2lg:tw-hidden">
  
                <a href="/en/portfolio" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  My Coins
  
</a>
              <a href="/en/nft-portfolio" data-view-component="true" class="dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  My NFTs
  
</a>

</div>

</div></div></div>        </div>


        <!-- My Account -->
        <div class="tw-flex tw-flex-col" data-action="click->navbar#handleClick" data-login-state-target="loggedInItem">
          <div class=" 2lg:tw-hidden tw-flex tw-items-center tw-cursor-pointer">
            <i data-view-component="true" class="fas fa-user-circle fa-fw tw-mr-2 tw-text-gray-900 dark:tw-text-moon-200"></i>

            <div data-view-component="true" class="nav-label dark:!tw-text-moon-50 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  My Account
</div>
            <i data-view-component="true" class="far nav-items-toggle fa-plus tw-text-lg tw-p-2 2lg:!tw-hidden tw-text-gray-700 dark:tw-text-moon-50"></i>

          </div>
          <div data-view-component="true" class="2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div data-view-component="true" class="tw-inline-block tw-text-left">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-navbar-target="accountMenu" data-view-component="true" class="nav-items 2lg:tw-hidden 2lg:!tw-w-52 dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true">
  
                <span data-action="click-&gt;application#navigateToUrl" data-url="/account/security" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Login and Security
  
</span>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/en/developers/dashboard" data-login-state-target="developerItem" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Developer&#39;s Dashboard
  
</span>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/en/premium/pricing" data-login-state-target="subscribeButton" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Upgrade to Premium
  
</span>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/account/subscriptions" data-login-state-target="premiumItem" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Manage Subscription
  
</span>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/account/premium-newsletter?locale=en" data-login-state-target="premiumItem" data-view-component="true" class="tw-cursor-pointer tw-hidden dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Premium Newsletter
  
</span>
              <span data-action="click-&gt;application#navigateToUrl" data-url="/account/sign_out?locale=en" data-method="delete" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Sign Out
  
</span>

              <div data-view-component="true" class="tw-mt-2 2lg:tw-hidden tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

</div>

</div></div></div>        </div>


        <div class="2lg:tw-hidden tw-mt-8 tw-grid tw-grid-cols-1 tw-gap-2" data-login-state-target="loggedOutItem">
          <button data-action="click-&gt;auth#openSignUpModal" data-analytics-origin="navbar_sign_up" type="button" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Create an account

</div></button>
          <button data-action="click-&gt;auth#openSignInModal" data-analytics-origin="navbar_login" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      Log in

</div></button>
        </div>
        <div class="2lg:tw-hidden tw-mt-8 tw-grid tw-grid-cols-3 tw-gap-x-2">
          <button onclick="Modal.show(&#39;language_selector&#39;)" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      EN

</div></button>
          <button onclick="Modal.show(&#39;currency_selector&#39;)" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      
            <span data-settings-target="currencyText">USD</span>


</div></button>          <button data-action="click-&gt;settings#toggleDarkMode" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      
            <i data-settings-target="darkModeButton" data-view-component="true" class="fas fa-fw fa-sun"></i>



</div></button>        </div>
      </div>

      <!-- Search -->
      <div data-controller="search-v2 button-ads targeting-ads"
     class="tw-flex flex-column tw-justify-center h-100 search-container tw-relative tw-py-2 2lg:tw-py-0">
  <div class="tw-relative tw-w-full" data-action="keydown->search-v2#onKeydown">
    <!-- Fake input to trigger search popover -->
    <div id="search-bar" class="tw-flex tw-items-center tw-justify-between tw-bg-gray-100 tw-p-2.5 tw-w-full 2lg:tw-w-52 tw-text-xs tw-text-inline tw-rounded-lg hover:tw-bg-gray-200 dark:tw-bg-moon-800 dark:hover:tw-bg-moon-700"
         data-action="click->search-v2#showSearchPopup click->button-ads#sendImpression"
         data-search-v2-target="searchbar inputOverlay"
         data-index-trending-coins-target="searchbar">
        <div class="tw-font-semibold tw-text-left tw-text-gray-500 dark:tw-text-moon-200">
          <i class="far fa-search tw-pr-1"></i>
          Search
        </div>
        <span class="tw-hidden lg:tw-block tw-py-0.5 tw-px-2 tw-rounded-md tw-rounder-2 tw-bg-gray-300 tw-text-gray-500 dark:tw-text-moon-200 dark:tw-bg-moon-600">
          /
        </span>
    </div>

    <!-- Search popover -->
    <div id="search-popover" class="search-results tw-w-full 2lg:tw-w-[768px] tw-max-h-[90vh] tw-right-0 tw-top-0 tw-rounded-md 2lg:tw-shadow-lg tw-hidden" data-search-v2-target="searchPopup">
      <!-- Search input field -->
      <div class="tw-flex tw-flex-row tw-items-center tw-px-2 2lg:tw-px-4 2lg:tw-py-2 tw-py-1 tw-shadow-sm 2lg:tw-shadow-none tw-rounded-lg">
        <div>
          <i class="far !tw-text-xs tw-ml-[2px] tw-mb-[5px] lg:tw-mb-0 lg:tw-mt-[2px] fa-search"></i>
        </div>
        <div class="tw-flex-1">
          <input id="search-input-field" class="tw-w-full tw-border-none tw-px-2 2lg:tw-py-2 search-input-dark dark:tw-text-white !tw-text-base 2lg:!tw-text-sm"
                 data-action="input->search-v2#onInputChanged focus->search-v2#onFocus"
                 data-search-v2-target="input"
                 placeholder="Search Token, Dex Pairs, NFT, Exchanges, Categories, Articles"
                 autocomplete="off"
            />
        </div>
        <div class="tw-flex tw-items-center">
          <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-action="click-&gt;search-v2#clearSearch" data-view-component="true" class="tw-cursor-pointer tw-mr-2 lg:tw-hidden tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-gray-100 dark:tw-bg-moon-400/20 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-700 dark:tw-text-moon-200 tw-font-medium">
  
      Clear

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

          <i data-action="click->search-v2#hideSearchPopup" class="fas fa-times tw-text-xl 2lg:tw-text-base tw-p-3 tw-pr-0 2lg:tw-p-2 2lg:tw-pr-0 tw-text-gray-500 tw-text-base dark:tw-text-white dark:tw-opacity-60 tw-cursor-pointer"></i>
        </div>
      </div>
      <div data-view-component="true" class="tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
      <div class="tw-flex tw-flex-col-reverse md:tw-grid md:tw-grid-cols-5">
        <div class="md:tw-col-span-3 md:tw-pt-4 md:tw-px-4">
          <div class="md:tw-mb-3">
            <div data-search-v2-target="defaultChips">
              <div x-data="{ activeTab: &#39;trending&#39; }" data-view-component="true">
  <nav class="tw-overflow-x-auto tw-flex tw-gap-x-2.5 tw-gap-y-1.5 tw-whitespace-nowrap">
      <a data-search-v2-target="chipTrendingCoin" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-coin-results" @click="activeTab = &#39;trending&#39;" :class="{ selected: activeTab === &#39;trending&#39; }" id="tab-trending" data-view-component="true" class="gecko-tab-chip-item selected">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-fire tw-mr-1' data-scroll-target='search-coin-results'></i>Trending
    

</span></a>

      <a data-search-v2-target="chipTrendingNft" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-nft-results" @click="activeTab = &#39;trending-nft&#39;" :class="{ selected: activeTab === &#39;trending-nft&#39; }" id="tab-trending-nft" data-view-component="true" class="gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-image tw-mr-1' data-scroll-target='search-nft-results'></i>NFTs
    

</span></a>

      <a data-search-v2-target="chipTrendingCategory" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-category-results" @click="activeTab = &#39;trending-categories&#39;" :class="{ selected: activeTab === &#39;trending-categories&#39; }" id="tab-trending-categories" data-view-component="true" class="gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-shapes tw-mr-1' data-scroll-target='search-category-results'></i>Categories
    

</span></a>

  </nav>

  <div data-view-component="true"></div></div>            </div>
            <div data-search-v2-target="userChips" class="tw-hidden">
              <div x-data="{ activeTab: &#39;cryptocurrencies&#39; }" data-view-component="true">
  <nav class="tw-overflow-x-auto tw-flex tw-gap-x-2.5 tw-gap-y-1.5 tw-whitespace-nowrap md:tw-flex-wrap md:tw-space-x-0">
      <a data-search-v2-target="chipCoin" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-coin-results" @click="activeTab = &#39;cryptocurrencies&#39;" :class="{ selected: activeTab === &#39;cryptocurrencies&#39; }" id="tab-cryptocurrencies" data-view-component="true" class="tw-hidden gecko-tab-chip-item selected">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-coins tw-mr-1' data-scroll-target='search-coin-results'></i>Cryptocurrencies
    

</span></a>

      <a data-search-v2-target="chipNft" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-nft_contract-results" @click="activeTab = &#39;nfts&#39;" :class="{ selected: activeTab === &#39;nfts&#39; }" id="tab-nfts" data-view-component="true" class="tw-hidden gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-image tw-mr-1' data-scroll-target='search-nft-results'></i>NFTs
    

</span></a>

      <a data-search-v2-target="chipExchange" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-market-results" @click="activeTab = &#39;exchanges&#39;" :class="{ selected: activeTab === &#39;exchanges&#39; }" id="tab-exchanges" data-view-component="true" class="tw-hidden gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-bank tw-mr-1' data-scroll-target='search-exchange-results'></i>Exchanges
    

</span></a>

      <a data-search-v2-target="chipCategory" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-category-results" @click="activeTab = &#39;categories&#39;" :class="{ selected: activeTab === &#39;categories&#39; }" id="tab-categories" data-view-component="true" class="tw-hidden gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-shapes tw-mr-1' data-scroll-target='search-category-results'></i>Categories
    

</span></a>

      <a data-search-v2-target="chipChain" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-asset_platform-results" @click="activeTab = &#39;chains&#39;" :class="{ selected: activeTab === &#39;chains&#39; }" id="tab-chains" data-view-component="true" class="tw-hidden gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-link tw-mr-1' data-scroll-target='search-chain-results'></i>Chains
    

</span></a>

      <a data-search-v2-target="chipArticle" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-post-results" @click="activeTab = &#39;articles&#39;" :class="{ selected: activeTab === &#39;articles&#39; }" id="tab-articles" data-view-component="true" class="tw-hidden gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-newspaper tw-mr-1' data-scroll-target='search-article-results'></i>Articles
    

</span></a>

      <a data-search-v2-target="chipGt" data-action="click-&gt;search-v2#scrollToList" data-scroll-target="search-gt-results" @click="activeTab = &#39;geckoterminal&#39;" :class="{ selected: activeTab === &#39;geckoterminal&#39; }" id="tab-geckoterminal" data-view-component="true" class="tw-hidden gecko-tab-chip-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <i class='fa-solid fa-chart-candlestick tw-mr-1' data-scroll-target='search-gt-results'></i>GeckoTerminal
    

</span></a>

  </nav>

  <div data-view-component="true"></div></div>            </div>
          </div>
          <!-- Search results box -->
          <div class="search-results-box tw-overflow-auto tw-h-full 2lg:tw-h-auto tw-pt-2 2lg:tw-pt-0"
            data-search-v2-target="results"
            data-action="mouseover->search-v2#onMouseover"
            data-url="https://www.coingecko.com/en/search_redirect"
            data-search-trending="{&quot;coins&quot;:[{&quot;item&quot;:{&quot;id&quot;:&quot;mantra-dao&quot;,&quot;coin_id&quot;:12151,&quot;name&quot;:&quot;MANTRA&quot;,&quot;symbol&quot;:&quot;OM&quot;,&quot;market_cap_rank&quot;:81,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/12151/standard/OM_Token.png?1696511991&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/12151/small/OM_Token.png?1696511991&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/12151/large/OM_Token.png?1696511991&quot;,&quot;slug&quot;:&quot;mantra&quot;,&quot;price_btc&quot;:1.9294290852055634e-05,&quot;score&quot;:0,&quot;data&quot;:{&quot;price&quot;:1.260800328906478,&quot;price_btc&quot;:&quot;0.0000192942908520556&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:6.784375254483462,&quot;ars&quot;:6.842237639828613,&quot;aud&quot;:5.865075348793369,&quot;bch&quot;:4.555773706794391,&quot;bdt&quot;:6.784212636466647,&quot;bhd&quot;:6.797411113813387,&quot;bmd&quot;:6.784375254483484,&quot;bnb&quot;:4.6588339806894945,&quot;brl&quot;:6.020446518289412,&quot;btc&quot;:3.7891533320401445,&quot;cad&quot;:6.836518848690869,&quot;chf&quot;:6.415889872052917,&quot;clp&quot;:5.700744117267221,&quot;cny&quot;:6.460933487622557,&quot;czk&quot;:6.354326655255369,&quot;dkk&quot;:6.441780476507689,&quot;dot&quot;:4.512548825733771,&quot;eos&quot;:5.151015039952896,&quot;eth&quot;:4.743790437084843,&quot;eur&quot;:6.451704019117107,&quot;gbp&quot;:6.175880770391213,&quot;gel&quot;:6.784375254483624,&quot;hkd&quot;:6.697644446602986,&quot;huf&quot;:6.673498743950601,&quot;idr&quot;:6.190892381017367,&quot;ils&quot;:5.277418516430251,&quot;inr&quot;:6.814609397850621,&quot;jpy&quot;:7.021570104444091,&quot;krw&quot;:5.262732456792517,&quot;kwd&quot;:6.717934005569777,&quot;lkr&quot;:6.335041872134926,&quot;ltc&quot;:6.026068585152673,&quot;mmk&quot;:6.7843752544841225,&quot;mxn&quot;:7.091079913869339,&quot;myr&quot;:7.146268562051232,&quot;ngn&quot;:7.090092643956389,&quot;nok&quot;:6.485493433907444,&quot;nzd&quot;:5.947240361748611,&quot;php&quot;:6.283264621797513,&quot;pkr&quot;:6.7411914442916245,&quot;pln&quot;:6.628773513679613,&quot;rub&quot;:6.9166684449267395,&quot;sar&quot;:6.7515611257409045,&quot;sek&quot;:6.1012698816121285,&quot;sgd&quot;:6.300116783895569,&quot;thb&quot;:5.667782738520518,&quot;try&quot;:6.788924146550111,&quot;twd&quot;:5.964764152285898,&quot;uah&quot;:6.617280830988716,&quot;usd&quot;:6.784375254483484,&quot;vef&quot;:6.784375254483423,&quot;vnd&quot;:6.9026886797781515,&quot;xag&quot;:5.643970288519663,&quot;xau&quot;:6.209092534368398,&quot;xdr&quot;:6.796932518513247,&quot;xlm&quot;:4.6522557972032255,&quot;xrp&quot;:5.760500666165131,&quot;yfi&quot;:3.09122686871684,&quot;zar&quot;:6.229955064651327,&quot;bits&quot;:3.7891533320401467,&quot;link&quot;:4.978182282164631,&quot;sats&quot;:3.789153332040139},&quot;market_cap&quot;:&quot;$1,062,702,927&quot;,&quot;market_cap_btc&quot;:&quot;16264.3425175931&quot;,&quot;total_volume&quot;:&quot;$42,920,810&quot;,&quot;total_volume_btc&quot;:&quot;656.826118923447&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/12151/sparkline.svg&quot;,&quot;content&quot;:null}}},{&quot;item&quot;:{&quot;id&quot;:&quot;clore-ai&quot;,&quot;coin_id&quot;:30959,&quot;name&quot;:&quot;Clore.ai&quot;,&quot;symbol&quot;:&quot;CLORE&quot;,&quot;market_cap_rank&quot;:695,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/30959/standard/CLORE_Logo_200x200_PNG.png?1696529798&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/30959/small/CLORE_Logo_200x200_PNG.png?1696529798&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/30959/large/CLORE_Logo_200x200_PNG.png?1696529798&quot;,&quot;slug&quot;:&quot;clore-ai&quot;,&quot;price_btc&quot;:1.6944068239438921e-06,&quot;score&quot;:1,&quot;data&quot;:{&quot;price&quot;:0.11072232181584614,&quot;price_btc&quot;:&quot;0.00000169440682394389&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:-0.2939606391948238,&quot;ars&quot;:-0.2443170328623144,&quot;aud&quot;:-1.188212059412579,&quot;bch&quot;:-2.412041636798884,&quot;bdt&quot;:-0.29411247787276124,&quot;bhd&quot;:-0.2817888781071533,&quot;bmd&quot;:-0.29396063919467597,&quot;bnb&quot;:-2.3163028492873052,&quot;brl&quot;:-1.0288355884447635,&quot;btc&quot;:-3.111025800274311,&quot;cad&quot;:-0.2588188833104277,&quot;chf&quot;:-0.608552548818337,&quot;clp&quot;:-1.3122369394437066,&quot;cny&quot;:-0.5931354728851509,&quot;czk&quot;:-0.713351325543885,&quot;dkk&quot;:-0.6352392411775878,&quot;dot&quot;:-2.462933049728366,&quot;eos&quot;:-1.8100407708809965,&quot;eth&quot;:-2.224214888921096,&quot;eur&quot;:-0.6265986089010452,&quot;gbp&quot;:-0.908096373846787,&quot;gel&quot;:-0.29396063919504556,&quot;hkd&quot;:-0.3722549264520579,&quot;huf&quot;:-0.4413462600132003,&quot;idr&quot;:-0.8794791506817511,&quot;ils&quot;:-1.7010268647665798,&quot;inr&quot;:-0.2715469930976903,&quot;jpy&quot;:-0.07327208973419265,&quot;krw&quot;:-1.7245985271695567,&quot;kwd&quot;:-0.3559977468109336,&quot;lkr&quot;:-0.7135093962091598,&quot;ltc&quot;:-1.01115206207429,&quot;mmk&quot;:-0.29396063919466103,&quot;mxn&quot;:-0.033094544118158396,&quot;myr&quot;:0.043944117777288585,&quot;ngn&quot;:-0.00850810931438006,&quot;nok&quot;:-0.5934987328779413,&quot;nzd&quot;:-1.1092712042618191,&quot;php&quot;:-0.7662780708444425,&quot;pkr&quot;:-0.33524292270794587,&quot;pln&quot;:-0.4720851260073022,&quot;rub&quot;:-0.17851119788793882,&quot;sar&quot;:-0.3245996423652907,&quot;sek&quot;:-0.919690493642799,&quot;sgd&quot;:-0.7558933922122091,&quot;thb&quot;:-1.3345302291057113,&quot;try&quot;:-0.2984469795536739,&quot;twd&quot;:-1.0557998311511083,&quot;uah&quot;:-0.44997899980413236,&quot;usd&quot;:-0.29396063919467597,&quot;vef&quot;:-0.2939606391946382,&quot;vnd&quot;:-0.23528478158947835,&quot;xag&quot;:-1.2097278566215224,&quot;xau&quot;:-0.7942511173104038,&quot;xdr&quot;:-0.2822357491193406,&quot;xlm&quot;:-2.3297465230362095,&quot;xrp&quot;:-1.2768863088622153,&quot;yfi&quot;:-3.7784557203272735,&quot;zar&quot;:-0.8302445131358295,&quot;bits&quot;:-3.111025800274306,&quot;link&quot;:-2.0251114919053923,&quot;sats&quot;:-3.1110258002743065},&quot;market_cap&quot;:&quot;$46,737,539&quot;,&quot;market_cap_btc&quot;:&quot;715.015294929257&quot;,&quot;total_volume&quot;:&quot;$4,313,860&quot;,&quot;total_volume_btc&quot;:&quot;66.0158958951883&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/30959/sparkline.svg&quot;,&quot;content&quot;:null}}},{&quot;item&quot;:{&quot;id&quot;:&quot;noisegpt&quot;,&quot;coin_id&quot;:29908,&quot;name&quot;:&quot;enqAI&quot;,&quot;symbol&quot;:&quot;ENQAI&quot;,&quot;market_cap_rank&quot;:871,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/29908/standard/icon.png?1702507913&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/29908/small/icon.png?1702507913&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/29908/large/icon.png?1702507913&quot;,&quot;slug&quot;:&quot;enqai&quot;,&quot;price_btc&quot;:4.789087171611198e-07,&quot;score&quot;:2,&quot;data&quot;:{&quot;price&quot;:0.031291624288025545,&quot;price_btc&quot;:&quot;0.00000047890871716112&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:7.997873208964405,&quot;ars&quot;:8.056393142627014,&quot;aud&quot;:7.068126376442152,&quot;bch&quot;:5.724222243888075,&quot;bdt&quot;:7.997708742956003,&quot;bhd&quot;:8.011057207838105,&quot;bmd&quot;:7.997873208964451,&quot;bnb&quot;:5.864997234746502,&quot;brl&quot;:7.225263184365277,&quot;btc&quot;:4.975668630011402,&quot;cad&quot;:8.050609363129823,&quot;chf&quot;:7.625200357564345,&quot;clp&quot;:6.901927684317545,&quot;cny&quot;:7.670755848913516,&quot;czk&quot;:7.562937536189746,&quot;dkk&quot;:7.6513851829240505,&quot;dot&quot;:5.674900185009755,&quot;eos&quot;:6.347075969608815,&quot;eth&quot;:5.926065749444014,&quot;eur&quot;:7.661421496701124,&quot;gbp&quot;:7.382463791765146,&quot;gel&quot;:7.997873208964426,&quot;hkd&quot;:7.9101567919280305,&quot;huf&quot;:7.885736697439621,&quot;idr&quot;:7.397645994378693,&quot;ils&quot;:6.473791410107375,&quot;inr&quot;:8.028450933225518,&quot;jpy&quot;:8.237763541897799,&quot;krw&quot;:6.458938458044973,&quot;kwd&quot;:7.930676921502494,&quot;lkr&quot;:7.543433600737397,&quot;ltc&quot;:7.2189154430094105,&quot;mmk&quot;:7.997873208964963,&quot;mxn&quot;:8.308063261001596,&quot;myr&quot;:8.36387907314418,&quot;ngn&quot;:8.307064771749765,&quot;nok&quot;:7.695594894500347,&quot;nzd&quot;:7.151225112847012,&quot;php&quot;:7.491067953574861,&quot;pkr&quot;:7.954198657826882,&quot;pln&quot;:7.840503209520283,&quot;rub&quot;:8.131669779612952,&quot;sar&quot;:7.964686180365875,&quot;sek&quot;:7.307005024626563,&quot;sgd&quot;:7.508111623692364,&quot;thb&quot;:6.868591732365159,&quot;try&quot;:8.00247379465406,&quot;twd&quot;:7.168948043790775,&quot;uah&quot;:7.828879923949897,&quot;usd&quot;:7.997873208964451,&quot;vef&quot;:7.997873208964486,&quot;vnd&quot;:8.117531148372468,&quot;xag&quot;:6.8445086776132635,&quot;xau&quot;:7.416052974325778,&quot;xdr&quot;:8.010573173779493,&quot;xlm&quot;:5.866184981779682,&quot;xrp&quot;:6.9823429745291525,&quot;yfi&quot;:4.174417915382085,&quot;zar&quot;:7.437152586464084,&quot;bits&quot;:4.97566863001141,&quot;link&quot;:6.133672520538485,&quot;sats&quot;:4.97566863001141},&quot;market_cap&quot;:&quot;$30,971,183&quot;,&quot;market_cap_btc&quot;:&quot;473.798476299128&quot;,&quot;total_volume&quot;:&quot;$1,026,086&quot;,&quot;total_volume_btc&quot;:&quot;15.703939113482&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/29908/sparkline.svg&quot;,&quot;content&quot;:null}}},{&quot;item&quot;:{&quot;id&quot;:&quot;spx6900&quot;,&quot;coin_id&quot;:31401,&quot;name&quot;:&quot;SPX6900&quot;,&quot;symbol&quot;:&quot;SPX&quot;,&quot;market_cap_rank&quot;:639,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/31401/standard/sticker_%281%29.jpg?1702371083&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/31401/small/sticker_%281%29.jpg?1702371083&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/31401/large/sticker_%281%29.jpg?1702371083&quot;,&quot;slug&quot;:&quot;spx6900&quot;,&quot;price_btc&quot;:9.127942420849793e-07,&quot;score&quot;:3,&quot;data&quot;:{&quot;price&quot;:0.05964145869991919,&quot;price_btc&quot;:&quot;0.000000912794242084979&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:42.009420608831356,&quot;ars&quot;:42.08637010446971,&quot;aud&quot;:40.78687052449816,&quot;bch&quot;:38.88014458971259,&quot;bdt&quot;:42.0092043478818,&quot;bhd&quot;:42.02675661727015,&quot;bmd&quot;:42.009420608831064,&quot;bnb&quot;:39.1575663281785,&quot;brl&quot;:40.993494103152486,&quot;btc&quot;:37.96669591222893,&quot;cad&quot;:42.07876485122793,&quot;chf&quot;:41.519382665198734,&quot;clp&quot;:40.56833122114628,&quot;cny&quot;:41.579284853453316,&quot;czk&quot;:41.437511541942506,&quot;dkk&quot;:41.55381382358716,&quot;dot&quot;:38.73148469396336,&quot;eos&quot;:39.700568565175956,&quot;eth&quot;:39.170531329318386,&quot;eur&quot;:41.56701085295615,&quot;gbp&quot;:41.20020157352089,&quot;gel&quot;:42.00942060883166,&quot;hkd&quot;:41.894079841544766,&quot;huf&quot;:41.861969177080006,&quot;idr&quot;:41.22016507588129,&quot;ils&quot;:40.005362873385344,&quot;inr&quot;:42.04962811270892,&quot;jpy&quot;:42.324859109398545,&quot;krw&quot;:39.98583231177235,&quot;kwd&quot;:41.92106233319129,&quot;lkr&quot;:41.4118652723364,&quot;ltc&quot;:41.00320830101961,&quot;mmk&quot;:42.00942060883087,&quot;mxn&quot;:42.417298174004735,&quot;myr&quot;:42.49069194471238,&quot;ngn&quot;:42.41598523259308,&quot;nok&quot;:41.611946408421424,&quot;nzd&quot;:40.89613937451849,&quot;php&quot;:41.34300821994871,&quot;pkr&quot;:41.9519917214086,&quot;pln&quot;:41.80249040013111,&quot;rub&quot;:42.185353457439085,&quot;sar&quot;:41.96578205778387,&quot;sek&quot;:41.10097873252605,&quot;sgd&quot;:41.36541941793382,&quot;thb&quot;:40.52449684662104,&quot;try&quot;:42.015470047480015,&quot;twd&quot;:40.91944375154007,&quot;uah&quot;:41.78720661721571,&quot;usd&quot;:42.009420608831064,&quot;vef&quot;:42.009420608830986,&quot;vnd&quot;:42.16676217623092,&quot;xag&quot;:40.492829365121786,&quot;xau&quot;:41.244368928047855,&quot;xdr&quot;:42.02612014736424,&quot;xlm&quot;:39.19881994239408,&quot;xrp&quot;:40.60397933583062,&quot;yfi&quot;:36.892542746308926,&quot;zar&quot;:41.272113397506274,&quot;bits&quot;:37.96669591222893,&quot;link&quot;:39.5284856966593,&quot;sats&quot;:37.96669591222894},&quot;market_cap&quot;:&quot;$55,529,628&quot;,&quot;market_cap_btc&quot;:&quot;849.608389222997&quot;,&quot;total_volume&quot;:&quot;$6,252,216&quot;,&quot;total_volume_btc&quot;:&quot;95.6882498456281&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/31401/sparkline.svg&quot;,&quot;content&quot;:null}}},{&quot;item&quot;:{&quot;id&quot;:&quot;hamster-kombat&quot;,&quot;coin_id&quot;:39102,&quot;name&quot;:&quot;Hamster Kombat&quot;,&quot;symbol&quot;:&quot;HMSTR&quot;,&quot;market_cap_rank&quot;:159,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/39102/standard/hamster-removebg-preview.png?1720514486&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/39102/small/hamster-removebg-preview.png?1720514486&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/39102/large/hamster-removebg-preview.png?1720514486&quot;,&quot;slug&quot;:&quot;hamster-kombat&quot;,&quot;price_btc&quot;:1.0898687811872588e-07,&quot;score&quot;:4,&quot;data&quot;:{&quot;price&quot;:0.0071211408776020385,&quot;price_btc&quot;:&quot;0.000000108986878118726&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:-42.85221593306943,&quot;ars&quot;:-42.897731695209195,&quot;aud&quot;:-42.901013383619684,&quot;bch&quot;:-43.72713940837845,&quot;bdt&quot;:-42.85213813864511,&quot;bhd&quot;:-42.86214479483102,&quot;bmd&quot;:-42.85213813864512,&quot;bnb&quot;:-43.782233246005944,&quot;brl&quot;:-43.23921698537092,&quot;btc&quot;:-43.6382801888192,&quot;cad&quot;:-42.80886840691614,&quot;chf&quot;:-42.8690677408157,&quot;clp&quot;:-42.99320665068931,&quot;cny&quot;:-42.84317031530515,&quot;czk&quot;:-42.9838769248609,&quot;dkk&quot;:-42.93224124675597,&quot;dot&quot;:-43.803433940508626,&quot;eos&quot;:-43.03370546455754,&quot;eth&quot;:-43.332297599006644,&quot;eur&quot;:-42.92920278026339,&quot;gbp&quot;:-42.99904152172835,&quot;gel&quot;:-42.85213813864494,&quot;hkd&quot;:-42.855054650236205,&quot;huf&quot;:-42.88562568247233,&quot;idr&quot;:-42.886455586310305,&quot;ils&quot;:-42.901684502106804,&quot;inr&quot;:-42.84098654471102,&quot;jpy&quot;:-42.57684318811691,&quot;krw&quot;:-43.21463518238685,&quot;kwd&quot;:-42.83940156951723,&quot;lkr&quot;:-42.85213813864512,&quot;ltc&quot;:-43.270499831122805,&quot;mmk&quot;:-42.85213813864493,&quot;mxn&quot;:-42.60160158105211,&quot;myr&quot;:-42.85213813864506,&quot;ngn&quot;:-42.610882498272574,&quot;nok&quot;:-42.971367636654804,&quot;nzd&quot;:-42.96789633673832,&quot;php&quot;:-42.949108263256235,&quot;pkr&quot;:-42.85213813864487,&quot;pln&quot;:-42.86901515540929,&quot;rub&quot;:-42.970866053864114,&quot;sar&quot;:-42.86240503524569,&quot;sek&quot;:-42.8797859442451,&quot;sgd&quot;:-42.89604369365702,&quot;thb&quot;:-42.91287287054261,&quot;try&quot;:-42.859861699797946,&quot;twd&quot;:-42.98918682114652,&quot;uah&quot;:-42.85213813864521,&quot;usd&quot;:-42.85213813864512,&quot;vef&quot;:-42.85213813864514,&quot;vnd&quot;:-42.85213813864523,&quot;xag&quot;:-41.73346086188564,&quot;xau&quot;:-42.54553444820374,&quot;xdr&quot;:-42.85213813864519,&quot;xlm&quot;:-43.23512019364828,&quot;xrp&quot;:-43.04131311183967,&quot;yfi&quot;:-42.92553168592475,&quot;zar&quot;:-43.00375236356058,&quot;bits&quot;:-43.638280188819195,&quot;link&quot;:-44.48170713011696,&quot;sats&quot;:-43.6382801888192},&quot;market_cap&quot;:&quot;$456,780,561&quot;,&quot;market_cap_btc&quot;:&quot;6988.78441034302&quot;,&quot;total_volume&quot;:&quot;$640,193,299&quot;,&quot;total_volume_btc&quot;:&quot;9797.96219355171&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/39102/sparkline.svg&quot;,&quot;content&quot;:null}}},{&quot;item&quot;:{&quot;id&quot;:&quot;self-chain&quot;,&quot;coin_id&quot;:38709,&quot;name&quot;:&quot;Self Chain&quot;,&quot;symbol&quot;:&quot;SLF&quot;,&quot;market_cap_rank&quot;:702,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/38709/standard/twD1uiHk_400x400.jpg?1718388886&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/38709/small/twD1uiHk_400x400.jpg?1718388886&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/38709/large/twD1uiHk_400x400.jpg?1718388886&quot;,&quot;slug&quot;:&quot;self-chain&quot;,&quot;price_btc&quot;:7.233596176979656e-06,&quot;score&quot;:5,&quot;data&quot;:{&quot;price&quot;:0.47268492576605503,&quot;price_btc&quot;:&quot;0.00000723359617697966&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:2.968989815309158,&quot;ars&quot;:3.020258043669401,&quot;aud&quot;:2.045473386705279,&quot;bch&quot;:0.7815931233086851,&quot;bdt&quot;:2.9688330076033886,&quot;bhd&quot;:2.9815599058623943,&quot;bmd&quot;:2.9689898153093046,&quot;bnb&quot;:0.8804650301601485,&quot;brl&quot;:2.210065565083745,&quot;btc&quot;:0.05973421013380773,&quot;cad&quot;:3.0052816099381197,&quot;chf&quot;:2.644102663581249,&quot;clp&quot;:1.9173897050081519,&quot;cny&quot;:2.6600242741970224,&quot;czk&quot;:2.535874272979334,&quot;dkk&quot;:2.6165426303940764,&quot;dot&quot;:0.7290362530005537,&quot;eos&quot;:1.403294892117236,&quot;eth&quot;:0.975566633973209,&quot;eur&quot;:2.625466033455576,&quot;gbp&quot;:2.3347560556292444,&quot;gel&quot;:2.9689898153089067,&quot;hkd&quot;:2.888133292285354,&quot;huf&quot;:2.816780896107642,&quot;idr&quot;:2.364309797604298,&quot;ils&quot;:1.5158763551899115,&quot;inr&quot;:2.992136963781742,&quot;jpy&quot;:3.1969005531886605,&quot;krw&quot;:1.491533293511202,&quot;kwd&quot;:2.9049224995954295,&quot;lkr&quot;:2.53571102934007,&quot;ltc&quot;:2.2283277973257745,&quot;mmk&quot;:2.9689898153093117,&quot;mxn&quot;:3.238392937319697,&quot;myr&quot;:3.3179527437562224,&quot;ngn&quot;:3.263783980541705,&quot;nok&quot;:2.6596491262647963,&quot;nzd&quot;:2.12699763701288,&quot;php&quot;:2.481215462612901,&quot;pkr&quot;:2.9263565399542473,&quot;pln&quot;:2.7850360790456814,&quot;rub&quot;:3.0882174210020645,&quot;sar&quot;:2.937348129152156,&quot;sek&quot;:2.322782510086312,&quot;sgd&quot;:2.4919399871770365,&quot;thb&quot;:1.8943668517198933,&quot;try&quot;:2.964356656298121,&quot;twd&quot;:2.1822188985186393,&quot;uah&quot;:2.8078656438189142,&quot;usd&quot;:2.9689898153093046,&quot;vef&quot;:2.968989815309344,&quot;vnd&quot;:3.0295858817350396,&quot;xag&quot;:2.0232534698589233,&quot;xau&quot;:2.4523269784737045,&quot;xdr&quot;:2.9810984106811764,&quot;xlm&quot;:0.8665814027068388,&quot;xrp&quot;:1.9538972099060223,&quot;yfi&quot;:-0.629537824749395,&quot;zar&quot;:2.4151556733860002,&quot;bits&quot;:0.05973421013379962,&quot;link&quot;:1.181185830071416,&quot;sats&quot;:0.05973421013379569},&quot;market_cap&quot;:&quot;$45,850,438&quot;,&quot;market_cap_btc&quot;:&quot;701.658829167027&quot;,&quot;total_volume&quot;:&quot;$36,040,584&quot;,&quot;total_volume_btc&quot;:&quot;551.536580429255&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/38709/sparkline.svg&quot;,&quot;content&quot;:null}}},{&quot;item&quot;:{&quot;id&quot;:&quot;derace&quot;,&quot;coin_id&quot;:17438,&quot;name&quot;:&quot;zkRace&quot;,&quot;symbol&quot;:&quot;ZERC&quot;,&quot;market_cap_rank&quot;:792,&quot;thumb&quot;:&quot;https://assets.coingecko.com/coins/images/17438/standard/zkRace-logomark-border.png?1716518566&quot;,&quot;small&quot;:&quot;https://assets.coingecko.com/coins/images/17438/small/zkRace-logomark-border.png?1716518566&quot;,&quot;large&quot;:&quot;https://assets.coingecko.com/coins/images/17438/large/zkRace-logomark-border.png?1716518566&quot;,&quot;slug&quot;:&quot;zkrace&quot;,&quot;price_btc&quot;:2.384012032227351e-06,&quot;score&quot;:6,&quot;data&quot;:{&quot;price&quot;:0.15578510645437937,&quot;price_btc&quot;:&quot;0.00000238401203222735&quot;,&quot;price_change_percentage_24h&quot;:{&quot;aed&quot;:16.519467367922395,&quot;ars&quot;:16.577482374888575,&quot;aud&quot;:15.474418343362098,&quot;bch&quot;:14.044214401651613,&quot;bdt&quot;:16.51928992469035,&quot;bhd&quot;:16.53369165291012,&quot;bmd&quot;:16.519467367922562,&quot;bnb&quot;:14.156097619547097,&quot;brl&quot;:15.660670466374896,&quot;btc&quot;:13.22736054857614,&quot;cad&quot;:16.5605350776045,&quot;chf&quot;:16.15182582902883,&quot;clp&quot;:15.32947914956558,&quot;cny&quot;:16.169842686258555,&quot;czk&quot;:16.02935483606637,&quot;dkk&quot;:16.120638960114505,&quot;dot&quot;:13.984741170479682,&quot;eos&quot;:14.747730665074235,&quot;eth&quot;:14.263714371367325,&quot;eur&quot;:16.13073666208963,&quot;gbp&quot;:15.80176993302273,&quot;gel&quot;:16.51946736792213,&quot;hkd&quot;:16.427970316112386,&quot;huf&quot;:16.347228111950106,&quot;idr&quot;:15.835212878125324,&quot;ils&quot;:14.875127584634768,&quot;inr&quot;:16.545660626843866,&quot;jpy&quot;:16.777370624357026,&quot;krw&quot;:14.8475810331342,&quot;kwd&quot;:16.44696894372648,&quot;lkr&quot;:16.02917010994703,&quot;ltc&quot;:15.681335965547088,&quot;mmk&quot;:16.519467367922598,&quot;mxn&quot;:16.824323308921997,&quot;myr&quot;:16.914352999283214,&quot;ngn&quot;:16.853055753878966,&quot;nok&quot;:16.1694181697383,&quot;nzd&quot;:15.566670993800342,&quot;php&quot;:15.967503054454404,&quot;pkr&quot;:16.471223653524355,&quot;pln&quot;:16.3113057514182,&quot;rub&quot;:16.654385046883892,&quot;sar&quot;:16.48366171008065,&quot;sek&quot;:15.788220696969518,&quot;sgd&quot;:15.979638901297518,&quot;thb&quot;:15.303426542783196,&quot;try&quot;:16.514224496052304,&quot;twd&quot;:15.629159243802377,&quot;uah&quot;:16.33713963337034,&quot;usd&quot;:16.519467367922562,&quot;vef&quot;:16.51946736792261,&quot;vnd&quot;:16.588037734565788,&quot;xag&quot;:15.449274337574122,&quot;xau&quot;:15.934812913558543,&quot;xdr&quot;:16.53316942604546,&quot;xlm&quot;:14.140386939284078,&quot;xrp&quot;:15.370790956482022,&quot;yfi&quot;:12.447381930545122,&quot;zar&quot;:15.892749951904186,&quot;bits&quot;:13.227360548576131,&quot;link&quot;:14.496392571405584,&quot;sats&quot;:13.22736054857614},&quot;market_cap&quot;:&quot;$37,194,103&quot;,&quot;market_cap_btc&quot;:&quot;549.319812523571&quot;,&quot;total_volume&quot;:&quot;$550,770&quot;,&quot;total_volume_btc&quot;:&quot;8.42854441882979&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/coins/17438/sparkline.svg&quot;,&quot;content&quot;:null}}}],&quot;nft&quot;:[{&quot;id&quot;:&quot;soulless-face&quot;,&quot;name&quot;:&quot;Soulless Face&quot;,&quot;symbol&quot;:&quot;SOUL&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/4896/standard/soulless-face.png?1724889691&quot;,&quot;nft_contract_id&quot;:4896,&quot;native_currency_symbol&quot;:&quot;eth&quot;,&quot;floor_price_in_native_currency&quot;:9.21,&quot;floor_price_24h_percentage_change&quot;:19143.2624589739,&quot;data&quot;:{&quot;floor_price&quot;:&quot;9,21 ETH&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;19143.2624589739&quot;,&quot;h24_volume&quot;:&quot;41,22 ETH&quot;,&quot;h24_average_sale_price&quot;:&quot;8,24 ETH&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/4896/sparkline.svg&quot;,&quot;content&quot;:null}},{&quot;id&quot;:&quot;lasercat-nft&quot;,&quot;name&quot;:&quot;LaserCat NFT&quot;,&quot;symbol&quot;:&quot;Cat&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/1142/standard/lasercat-nft.png?1707287668&quot;,&quot;nft_contract_id&quot;:1142,&quot;native_currency_symbol&quot;:&quot;eth&quot;,&quot;floor_price_in_native_currency&quot;:19.99,&quot;floor_price_24h_percentage_change&quot;:126.781046769953,&quot;data&quot;:{&quot;floor_price&quot;:&quot;19,99 ETH&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;126.781046769953&quot;,&quot;h24_volume&quot;:&quot;9,00 ETH&quot;,&quot;h24_average_sale_price&quot;:&quot;9,00 ETH&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/1142/sparkline.svg&quot;,&quot;content&quot;:null}},{&quot;id&quot;:&quot;blob&quot;,&quot;name&quot;:&quot;Blob&quot;,&quot;symbol&quot;:&quot;BLOBARMY&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/4428/standard/blob.jpg?1717744245&quot;,&quot;nft_contract_id&quot;:4428,&quot;native_currency_symbol&quot;:&quot;btc&quot;,&quot;floor_price_in_native_currency&quot;:0.00849,&quot;floor_price_24h_percentage_change&quot;:41.7586959314243,&quot;data&quot;:{&quot;floor_price&quot;:&quot;0,008 BTC&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;41.7586959314243&quot;,&quot;h24_volume&quot;:&quot;0,56 BTC&quot;,&quot;h24_average_sale_price&quot;:&quot;0,007 BTC&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/4428/sparkline.svg&quot;,&quot;content&quot;:null}},{&quot;id&quot;:&quot;onchain-gaias&quot;,&quot;name&quot;:&quot;onchain gaias&quot;,&quot;symbol&quot;:&quot;EARLY&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/4571/standard/onchain-gaias.png?1720149854&quot;,&quot;nft_contract_id&quot;:4571,&quot;native_currency_symbol&quot;:&quot;eth&quot;,&quot;floor_price_in_native_currency&quot;:0.3468777,&quot;floor_price_24h_percentage_change&quot;:36.5735907953717,&quot;data&quot;:{&quot;floor_price&quot;:&quot;0,35 ETH&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;36.5735907953717&quot;,&quot;h24_volume&quot;:&quot;6,91 ETH&quot;,&quot;h24_average_sale_price&quot;:&quot;0,35 ETH&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/4571/sparkline.svg&quot;,&quot;content&quot;:null}},{&quot;id&quot;:&quot;runestone&quot;,&quot;name&quot;:&quot;Runestone&quot;,&quot;symbol&quot;:&quot;RUNESTONE&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/4200/standard/runestone.png?1710468413&quot;,&quot;nft_contract_id&quot;:4200,&quot;native_currency_symbol&quot;:&quot;btc&quot;,&quot;floor_price_in_native_currency&quot;:0.008399,&quot;floor_price_24h_percentage_change&quot;:23.4964343332158,&quot;data&quot;:{&quot;floor_price&quot;:&quot;0,008 BTC&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;23.4964343332158&quot;,&quot;h24_volume&quot;:&quot;4,33 BTC&quot;,&quot;h24_average_sale_price&quot;:&quot;0,009 BTC&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/4200/sparkline.svg&quot;,&quot;content&quot;:null}},{&quot;id&quot;:&quot;nakamigos&quot;,&quot;name&quot;:&quot;Nakamigos&quot;,&quot;symbol&quot;:&quot;NKMGS&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/3134/standard/nakamigos.png?1707289851&quot;,&quot;nft_contract_id&quot;:3134,&quot;native_currency_symbol&quot;:&quot;eth&quot;,&quot;floor_price_in_native_currency&quot;:0.156,&quot;floor_price_24h_percentage_change&quot;:18.9996614049686,&quot;data&quot;:{&quot;floor_price&quot;:&quot;0,16 ETH&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;18.9996614049686&quot;,&quot;h24_volume&quot;:&quot;6,20 ETH&quot;,&quot;h24_average_sale_price&quot;:&quot;0,16 ETH&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/3134/sparkline.svg&quot;,&quot;content&quot;:null}},{&quot;id&quot;:&quot;o-p-i-u-m&quot;,&quot;name&quot;:&quot;O.P.I.U.M.&quot;,&quot;symbol&quot;:&quot;OPIUM&quot;,&quot;thumb&quot;:&quot;https://assets.coingecko.com/nft_contracts/images/3874/standard/o-p-i-u-m.jpg?1707290229&quot;,&quot;nft_contract_id&quot;:3874,&quot;native_currency_symbol&quot;:&quot;btc&quot;,&quot;floor_price_in_native_currency&quot;:0.179,&quot;floor_price_24h_percentage_change&quot;:18.4692357316584,&quot;data&quot;:{&quot;floor_price&quot;:&quot;0,18 BTC&quot;,&quot;floor_price_in_usd_24h_percentage_change&quot;:&quot;18.4692357316584&quot;,&quot;h24_volume&quot;:&quot;0,62 BTC&quot;,&quot;h24_average_sale_price&quot;:&quot;0,15 BTC&quot;,&quot;sparkline&quot;:&quot;https://www.coingecko.com/nft/3874/sparkline.svg&quot;,&quot;content&quot;:null}}],&quot;exchanges&quot;:[]}"
            data-search-trending-categories="[{&quot;id&quot;:244,&quot;name&quot;:&quot;Data Availability&quot;,&quot;market_cap_1h_change&quot;:1.5762264184483206,&quot;slug&quot;:&quot;data-availability&quot;,&quot;coins_count&quot;:10,&quot;data&quot;:{&quot;market_cap&quot;:7877826597.521575,&quot;market_cap_btc&quot;:123548.99729217237,&quot;total_volume&quot;:641029296.5135735,&quot;total_volume_btc&quot;:10053.347308263312,&quot;market_cap_change_percentage_24h&quot;:{&quot;aed&quot;:1.3772392387079397,&quot;ars&quot;:1.7187749899289193,&quot;aud&quot;:1.9291362000485275,&quot;bch&quot;:1.5115847486116056,&quot;bdt&quot;:1.354136700866832,&quot;bhd&quot;:1.385018791183131,&quot;bmd&quot;:1.3764112255482086,&quot;bnb&quot;:3.413455100942156,&quot;brl&quot;:1.8190566050345909,&quot;btc&quot;:2.203692447744023,&quot;cad&quot;:1.7261452468465097,&quot;chf&quot;:2.1142343192105693,&quot;clp&quot;:1.170048158909625,&quot;cny&quot;:1.206277869582972,&quot;czk&quot;:2.038020843308542,&quot;dkk&quot;:1.7738574967982719,&quot;dot&quot;:-1.5220431480993788,&quot;eos&quot;:-0.49068435302305,&quot;eth&quot;:2.668591303755342,&quot;eur&quot;:1.7788232781609297,&quot;gbp&quot;:1.8861708030291624,&quot;gel&quot;:1.376411225548174,&quot;hkd&quot;:1.3526659252050046,&quot;huf&quot;:2.1148643039555175,&quot;idr&quot;:1.2425907348776353,&quot;ils&quot;:0.19922556950113857,&quot;inr&quot;:1.4457799972729228,&quot;jpy&quot;:2.665728805691195,&quot;krw&quot;:1.617530387718337,&quot;kwd&quot;:1.3847171999678394,&quot;lkr&quot;:1.0780009266882298,&quot;ltc&quot;:0.2736514513800166,&quot;mmk&quot;:1.3764112255482648,&quot;mxn&quot;:2.7551824631575785,&quot;myr&quot;:1.1933111450683649,&quot;ngn&quot;:3.6332123552547757,&quot;nok&quot;:3.172168611498298,&quot;nzd&quot;:2.41241253142227,&quot;php&quot;:1.5168763009463,&quot;pkr&quot;:1.8125896795582748,&quot;pln&quot;:2.102129954100967,&quot;rub&quot;:1.0505831836202022,&quot;sar&quot;:1.3702232534955279,&quot;sek&quot;:2.0846284631488303,&quot;sgd&quot;:1.6971080842208193,&quot;thb&quot;:1.2652204816710528,&quot;try&quot;:1.5235664269352869,&quot;twd&quot;:1.623173712568231,&quot;uah&quot;:1.603721785849906,&quot;usd&quot;:1.3764112255482086,&quot;vef&quot;:1.3764112255481105,&quot;vnd&quot;:1.488760476391912,&quot;xag&quot;:1.1320199748584996,&quot;xau&quot;:1.0153054251753764,&quot;xdr&quot;:1.835900410846338,&quot;xlm&quot;:1.006891968855415,&quot;xrp&quot;:2.0923986494330857,&quot;yfi&quot;:-1.9526119805893547,&quot;zar&quot;:1.2737293293269265,&quot;bits&quot;:2.2036924477440225,&quot;link&quot;:0.7804193853386644,&quot;sats&quot;:2.2036924477440203},&quot;sparkline&quot;:&quot;https://www.coingecko.com/categories/35572024/sparkline.svg&quot;}},{&quot;id&quot;:268,&quot;name&quot;:&quot;LRTfi&quot;,&quot;market_cap_1h_change&quot;:1.032433490459856,&quot;slug&quot;:&quot;lrtfi&quot;,&quot;coins_count&quot;:4,&quot;data&quot;:{&quot;market_cap&quot;:712901102.0181477,&quot;market_cap_btc&quot;:11179.428333261238,&quot;total_volume&quot;:211896890.49182773,&quot;total_volume_btc&quot;:3322.88180588896,&quot;market_cap_change_percentage_24h&quot;:{&quot;aed&quot;:5.12273915761264,&quot;ars&quot;:5.476893344077118,&quot;aud&quot;:5.695026593575216,&quot;bch&quot;:5.253322968691446,&quot;bdt&quot;:5.098783069662476,&quot;bhd&quot;:5.130806134694874,&quot;bmd&quot;:5.121880552544376,&quot;bnb&quot;:7.222584344077696,&quot;brl&quot;:5.580879979994735,&quot;btc&quot;:5.969356524053387,&quot;cad&quot;:5.48453590370188,&quot;chf&quot;:5.886963377860903,&quot;clp&quot;:4.90789316258482,&quot;cny&quot;:4.945461422023049,&quot;czk&quot;:5.807934106519984,&quot;dkk&quot;:5.5340109381767,&quot;dot&quot;:2.1129737265911617,&quot;eos&quot;:3.194243342429013,&quot;eth&quot;:6.457118740303226,&quot;eur&quot;:5.5391601861027935,&quot;gbp&quot;:5.650473790030757,&quot;gel&quot;:5.121880552544168,&quot;hkd&quot;:5.097257954484475,&quot;huf&quot;:5.887616638124157,&quot;idr&quot;:4.983115908327062,&quot;ils&quot;:3.901202404372259,&quot;inr&quot;:5.193812234157188,&quot;jpy&quot;:6.458833469062092,&quot;krw&quot;:5.371908142376802,&quot;kwd&quot;:5.1304934008417185,&quot;lkr&quot;:4.8124451383961455,&quot;ltc&quot;:3.972750503072494,&quot;mmk&quot;:5.121880552544955,&quot;mxn&quot;:6.551592095861427,&quot;myr&quot;:4.93201562680214,&quot;ngn&quot;:7.462061822721321,&quot;nok&quot;:6.9839842820520746,&quot;nzd&quot;:6.196158130649622,&quot;php&quot;:5.267535273394182,&quot;pkr&quot;:5.574174126441397,&quot;pln&quot;:5.874411802915279,&quot;rub&quot;:4.784014414947476,&quot;sar&quot;:5.115463958672649,&quot;sek&quot;:5.856263699040561,&quot;sgd&quot;:5.454425929357516,&quot;thb&quot;:5.006581737414723,&quot;try&quot;:5.274472573862845,&quot;twd&quot;:5.377759966421447,&quot;uah&quot;:5.357589365664512,&quot;usd&quot;:5.121880552544376,&quot;vef&quot;:5.121880552544346,&quot;vnd&quot;:5.238380677026773,&quot;xag&quot;:4.868459983079372,&quot;xau&quot;:4.747433278718817,&quot;xdr&quot;:5.598346099787316,&quot;xlm&quot;:4.7845638008662466,&quot;xrp&quot;:5.852655030309123,&quot;yfi&quot;:1.640802999553833,&quot;zar&quot;:5.015404954335547,&quot;bits&quot;:5.969356524053394,&quot;link&quot;:4.505346203259717,&quot;sats&quot;:5.969356524053389},&quot;sparkline&quot;:&quot;https://www.coingecko.com/categories/35572128/sparkline.svg&quot;}},{&quot;id&quot;:400,&quot;name&quot;:&quot;Yield Tokenization Protocol&quot;,&quot;market_cap_1h_change&quot;:1.0307832035739615,&quot;slug&quot;:&quot;yield-tokenization&quot;,&quot;coins_count&quot;:3,&quot;data&quot;:{&quot;market_cap&quot;:705545714.1791934,&quot;market_cap_btc&quot;:11062.4171106316,&quot;total_volume&quot;:212037192.37588492,&quot;total_volume_btc&quot;:3324.580984462661,&quot;market_cap_change_percentage_24h&quot;:{&quot;aed&quot;:5.216898444403887,&quot;ars&quot;:5.571369849634359,&quot;aud&quot;:5.789698482846516,&quot;bch&quot;:5.343886719813617,&quot;bdt&quot;:5.192920898791893,&quot;bhd&quot;:5.224972647142418,&quot;bmd&quot;:5.2160390702758574,&quot;bnb&quot;:7.3036908541944845,&quot;brl&quot;:5.675449627221731,&quot;btc&quot;:6.048090425022989,&quot;cad&quot;:5.579019254761559,&quot;chf&quot;:5.981807186460355,&quot;clp&quot;:5.001860010082224,&quot;cny&quot;:5.039461919714249,&quot;czk&quot;:5.902707127962828,&quot;dkk&quot;:5.628538604424492,&quot;dot&quot;:2.207538315575377,&quot;eos&quot;:3.2727913510296904,&quot;eth&quot;:6.556247439079692,&quot;eur&quot;:5.6336924645734054,&quot;gbp&quot;:5.745105772995859,&quot;gel&quot;:5.216039070275701,&quot;hkd&quot;:5.191394417556239,&quot;huf&quot;:5.982461031854165,&quot;idr&quot;:5.077150133445609,&quot;ils&quot;:3.9942675508240524,&quot;inr&quot;:5.288035181677097,&quot;jpy&quot;:6.554189506322751,&quot;krw&quot;:5.466290611840607,&quot;kwd&quot;:5.224659633171145,&quot;lkr&quot;:4.906326492327558,&quot;ltc&quot;:4.04748315927574,&quot;mmk&quot;:5.216039070275627,&quot;mxn&quot;:6.6470312177732165,&quot;myr&quot;:5.026004080986057,&quot;ngn&quot;:7.558316459723696,&quot;nok&quot;:7.0798107011388085,&quot;nzd&quot;:6.291278887488236,&quot;php&quot;:5.361824255235954,&quot;pkr&quot;:5.6687377671815,&quot;pln&quot;:5.969244368968028,&quot;rub&quot;:4.8778703032497095,&quot;sar&quot;:5.2096167290096265,&quot;sek&quot;:5.95108000968974,&quot;sgd&quot;:5.548882310669793,&quot;thb&quot;:5.100636981065384,&quot;try&quot;:5.368767769500845,&quot;twd&quot;:5.472147677412184,&quot;uah&quot;:5.451959009684072,&quot;usd&quot;:5.2160390702758574,&quot;vef&quot;:5.216039070275859,&quot;vnd&quot;:5.33264354486121,&quot;xag&quot;:4.962391509959921,&quot;xau&quot;:4.841256401002006,&quot;xdr&quot;:5.692931391559069,&quot;xlm&quot;:4.88858511306508,&quot;xrp&quot;:5.905308193858658,&quot;yfi&quot;:1.724118231540431,&quot;zar&quot;:5.109468101014251,&quot;bits&quot;:6.048090425023003,&quot;link&quot;:4.626175151584106,&quot;sats&quot;:6.048090425023},&quot;sparkline&quot;:&quot;https://www.coingecko.com/categories/35572239/sparkline.svg&quot;}},{&quot;id&quot;:479,&quot;name&quot;:&quot;Tap to Earn&quot;,&quot;market_cap_1h_change&quot;:1.0161317272731383,&quot;slug&quot;:&quot;tap-to-earn&quot;,&quot;coins_count&quot;:5,&quot;data&quot;:{&quot;market_cap&quot;:1031756587.6712115,&quot;market_cap_btc&quot;:16177.154080992752,&quot;total_volume&quot;:492342482.00144285,&quot;total_volume_btc&quot;:7719.553514005614,&quot;market_cap_change_percentage_24h&quot;:{&quot;aed&quot;:6.905687910506271,&quot;ars&quot;:7.2658487780192935,&quot;aud&quot;:7.487681706657077,&quot;bch&quot;:7.034714418034619,&quot;bdt&quot;:6.8813255120136665,&quot;bhd&quot;:6.913891708668479,&quot;bmd&quot;:6.904814742947729,&quot;bnb&quot;:9.02597449368251,&quot;brl&quot;:7.371599093653518,&quot;btc&quot;:7.7502209825463435,&quot;cad&quot;:7.273620960333344,&quot;chf&quot;:7.682873861311612,&quot;clp&quot;:6.687197990272578,&quot;cny&quot;:6.725403431369882,&quot;czk&quot;:7.602504203086936,&quot;dkk&quot;:7.3239351229713465,&quot;dot&quot;:3.848025885685625,&quot;eos&quot;:4.93037682206277,&quot;eth&quot;:8.266534197984676,&quot;eur&quot;:7.3291717054287195,&quot;gbp&quot;:7.442373259127642,&quot;gel&quot;:6.904814742947593,&quot;hkd&quot;:6.879774529909175,&quot;huf&quot;:7.683538201285966,&quot;idr&quot;:6.763696561795113,&quot;ils&quot;:5.663433114259308,&quot;inr&quot;:6.977966431792669,&quot;jpy&quot;:8.264443234267782,&quot;krw&quot;:7.159082960289085,&quot;kwd&quot;:6.9135736706496695,&quot;lkr&quot;:6.590131106672405,&quot;ltc&quot;:5.717502862685799,&quot;mmk&quot;:6.904814742947522,&quot;mxn&quot;:8.35877510658241,&quot;myr&quot;:6.711729586880109,&quot;ngn&quot;:9.28468698113635,&quot;nok&quot;:8.798500940234526,&quot;nzd&quot;:7.997312754458649,&quot;php&quot;:7.052939860830354,&quot;pkr&quot;:7.364779504544096,&quot;pln&quot;:7.67010940364403,&quot;rub&quot;:6.561218180007054,&quot;sar&quot;:6.898289319548908,&quot;sek&quot;:7.651653496343876,&quot;sgd&quot;:7.243000301605663,&quot;thb&quot;:6.787560386321056,&quot;try&quot;:7.059994822342987,&quot;twd&quot;:7.16503403500545,&quot;uah&quot;:7.144521327984236,&quot;usd&quot;:6.904814742947729,&quot;vef&quot;:6.904814742947732,&quot;vnd&quot;:7.023290783900206,&quot;xag&quot;:6.647095998874272,&quot;xau&quot;:6.524016604359511,&quot;xdr&quot;:7.389361449986062,&quot;xlm&quot;:6.572104968451482,&quot;xrp&quot;:7.605147017530291,&quot;yfi&quot;:3.3568466416897826,&quot;zar&quot;:6.796533250633841,&quot;bits&quot;:7.750220982546348,&quot;link&quot;:6.305483181823569,&quot;sats&quot;:7.750220982546346},&quot;sparkline&quot;:&quot;https://www.coingecko.com/categories/35572253/sparkline.svg&quot;}},{&quot;id&quot;:184,&quot;name&quot;:&quot;Fixed Interest&quot;,&quot;market_cap_1h_change&quot;:1.0136115437499509,&quot;slug&quot;:&quot;fixed-interest&quot;,&quot;coins_count&quot;:11,&quot;data&quot;:{&quot;market_cap&quot;:738937234.4033198,&quot;market_cap_btc&quot;:11587.716488871249,&quot;total_volume&quot;:213121243.63929945,&quot;total_volume_btc&quot;:3342.0816194788326,&quot;market_cap_change_percentage_24h&quot;:{&quot;aed&quot;:4.916028390404738,&quot;ars&quot;:5.269486176792548,&quot;aud&quot;:5.487190494437147,&quot;bch&quot;:5.051698591959468,&quot;bdt&quot;:4.89211940911626,&quot;bhd&quot;:4.924079504781774,&quot;bmd&quot;:4.915171473676165,&quot;bnb&quot;:7.027592377397834,&quot;brl&quot;:5.373268335948248,&quot;btc&quot;:5.761631755481264,&quot;cad&quot;:5.277113708276094,&quot;chf&quot;:5.678749858953691,&quot;clp&quot;:4.701604863254054,&quot;cny&quot;:4.739099249391613,&quot;czk&quot;:5.5998759888276455,&quot;dkk&quot;:5.326491456260742,&quot;dot&quot;:1.9132188766519644,&quot;eos&quot;:2.9916740648216993,&quot;eth&quot;:6.252818643538573,&quot;eur&quot;:5.331630578832466,&quot;gbp&quot;:5.442725298429125,&quot;gel&quot;:4.915171473676033,&quot;hkd&quot;:4.89059729288731,&quot;huf&quot;:5.67940183466211,&quot;idr&quot;:4.7766796928402595,&quot;ils&quot;:3.696893636973685,&quot;inr&quot;:4.986961710600606,&quot;jpy&quot;:6.249495438881269,&quot;krw&quot;:5.164707415409177,&quot;kwd&quot;:4.923767385880552,&quot;lkr&quot;:4.606344525711256,&quot;ltc&quot;:3.7696421455989206,&quot;mmk&quot;:4.915171473676299,&quot;mxn&quot;:6.342071667399608,&quot;myr&quot;:4.725679893651524,&quot;ngn&quot;:7.250751068994803,&quot;nok&quot;:6.773613608236707,&quot;nzd&quot;:5.987336618790547,&quot;php&quot;:5.060539782667605,&quot;pkr&quot;:5.366575668620299,&quot;pln&quot;:5.666222965116138,&quot;rub&quot;:4.577969707737349,&quot;sar&quot;:4.908767497236722,&quot;sek&quot;:5.648110547226281,&quot;sgd&quot;:5.247062941444428,&quot;thb&quot;:4.800099379298964,&quot;try&quot;:5.067463441799356,&quot;twd&quot;:5.1705477325714,&quot;uah&quot;:5.150416794786773,&quot;usd&quot;:4.915171473676165,&quot;vef&quot;:4.915171473676067,&quot;vnd&quot;:5.03144251518139,&quot;xag&quot;:4.662249224182474,&quot;xau&quot;:4.541460503754936,&quot;xdr&quot;:5.390700110792769,&quot;xlm&quot;:4.585317431410927,&quot;xrp&quot;:5.640969203030494,&quot;yfi&quot;:1.4415632101173914,&quot;zar&quot;:4.808905246464035,&quot;bits&quot;:5.761631755481258,&quot;link&quot;:4.307663562770713,&quot;sats&quot;:5.761631755481257},&quot;sparkline&quot;:&quot;https://www.coingecko.com/categories/35572146/sparkline.svg&quot;}},{&quot;id&quot;:181,&quot;name&quot;:&quot;Zero Knowledge (ZK)&quot;,&quot;market_cap_1h_change&quot;:0.9921848381509751,&quot;slug&quot;:&quot;zero-knowledge-zk&quot;,&quot;coins_count&quot;:49,&quot;data&quot;:{&quot;market_cap&quot;:14189551834.86947,&quot;market_cap_btc&quot;:222514.8444432908,&quot;total_volume&quot;:915468642.0857296,&quot;total_volume_btc&quot;:14356.011018320556,&quot;market_cap_change_percentage_24h&quot;:{&quot;aed&quot;:1.4692992234426927,&quot;ars&quot;:1.811145120967484,&quot;aud&quot;:2.0216973586780873,&quot;bch&quot;:1.5953447194626023,&quot;bdt&quot;:1.4461757063433678,&quot;bhd&quot;:1.4770858404767022,&quot;bmd&quot;:1.4684704583697548,&quot;bnb&quot;:3.4961663052532947,&quot;brl&quot;:1.911517801128941,&quot;btc&quot;:2.286493215642025,&quot;cad&quot;:1.818522070765529,&quot;chf&quot;:2.2069635641892584,&quot;clp&quot;:1.2619199948273425,&quot;cny&quot;:1.298182605455536,&quot;czk&quot;:2.1306808793452077,&quot;dkk&quot;:1.866277647888454,&quot;dot&quot;:-1.4358646978931373,&quot;eos&quot;:-0.39217357007568604,&quot;eth&quot;:2.7573037240738887,&quot;eur&quot;:1.8712479386435752,&quot;gbp&quot;:1.9786929450724342,&quot;gel&quot;:1.4684704583695292,&quot;hkd&quot;:1.4447035950800153,&quot;huf&quot;:2.207594121018863,&quot;idr&quot;:1.334528446217526,&quot;ils&quot;:0.2902158079968441,&quot;inr&quot;:1.5379022234065425,&quot;jpy&quot;:2.7589588590800096,&quot;krw&quot;:1.7098085792189763,&quot;kwd&quot;:1.4767839753885228,&quot;lkr&quot;:1.1697891751370026,&quot;ltc&quot;:0.3592773211771395,&quot;mmk&quot;:1.4684704583703112,&quot;mxn&quot;:2.8484937488068236,&quot;myr&quot;:1.2852041059463108,&quot;ngn&quot;:3.7273209739052717,&quot;nok&quot;:3.2658585594466625,&quot;nzd&quot;:2.5054125500171134,&quot;php&quot;:1.6090630891521,&quot;pkr&quot;:1.9050450030815822,&quot;pln&quot;:2.1948482071876203,&quot;rub&quot;:1.1423465342025017,&quot;sar&quot;:1.4622768670612902,&quot;sek&quot;:2.177330823249967,&quot;sgd&quot;:1.7894585396889853,&quot;thb&quot;:1.3571787429307174,&quot;try&quot;:1.615759290399307,&quot;twd&quot;:1.7154570287337796,&quot;uah&quot;:1.6959874378524573,&quot;usd&quot;:1.4684704583697548,&quot;vef&quot;:1.4684704583696977,&quot;vnd&quot;:1.5809217328076137,&quot;xag&quot;:1.2238572776394845,&quot;xau&quot;:1.1070367402638794,&quot;xdr&quot;:1.9283769026868829,&quot;xlm&quot;:1.142876826740815,&quot;xrp&quot;:2.1738475703377778,&quot;yfi&quot;:-1.8916255843600385,&quot;zar&quot;:1.365695317413338,&quot;bits&quot;:2.2864932156420124,&quot;link&quot;:0.8733631688298583,&quot;sats&quot;:2.2864932156420212},&quot;sparkline&quot;:&quot;https://www.coingecko.com/categories/35572132/sparkline.svg&quot;}}]">
          </div>
        </div>
        <div class="md:tw-col-span-2 md:tw-px-4 md:tw-border-l md:tw-border-gray-200 dark:md:tw-border-moon-700">
          <div class="tw-mb-5">
            <div id="sponsored-search-desktop"
              class="tw-pt-4 md:tw-block"
              data-button-ads-target="body"
              data-login-state-target="kevelAd"
              data-ad-prop="{&quot;requestBody&quot;:{&quot;placements&quot;:[{&quot;count&quot;:1,&quot;siteId&quot;:1267711,&quot;adTypes&quot;:[2776],&quot;divName&quot;:&quot;multiWinner&quot;,&quot;zoneIds&quot;:[304109],&quot;networkId&quot;:11401}]},&quot;templateName&quot;:&quot;searchNew&quot;}"
              data-cg-logo-url="https://static.coingecko.com/s/gecko-65456030ba03df0f83f96e18d0c8449485c1a61dbdeeb733ca69164982489d0e.svg"
              data-sponsored="Sponsored"
              data-search-v2-target="searchAd">
            </div>
          </div>
          <div data-search-v2-target="smartResult" class="tw-hidden md:tw-block">
          </div>
        </div>
      </div>
      <div class="tw-hidden md:tw-flex tw-flex-row tw-gap-4 tw-items-center tw-py-2 tw-px-4 tw-bg-gray-100 dark:tw-bg-moon-700 tailwind-reset">
        <div class="tw-flex tw-flex-row tw-items-center tw-gap-1">
          <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-view-component="true" class="!tw-px-2 tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-gray-400 dark:tw-bg-moon-500 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white dark:tw-text-moon-50 tw-font-medium">
  
      <i class="far fa-fa-regular fa-arrow-up"></i>

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

          <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-view-component="true" class="!tw-px-2 tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-gray-400 dark:tw-bg-moon-500 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white dark:tw-text-moon-50 tw-font-medium">
  
      <i class="far fa-fa-regular fa-arrow-down"></i>

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

          <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium">
  Move
</div>
        </div>
        <div class="tw-flex tw-flex-row tw-items-center tw-gap-1">
          <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-view-component="true" class="!tw-px-2 tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-gray-400 dark:tw-bg-moon-500 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white dark:tw-text-moon-50 tw-font-medium">
  
      <i class="far fa-fa-regular fa-arrow-turn-down-left"></i>

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

          <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium">
  Select
</div>
        </div>
        <div class="tw-flex tw-flex-row tw-items-center tw-gap-1">
          <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-view-component="true" class="!tw-px-2 tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-gray-400 dark:tw-bg-moon-500 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white dark:tw-text-moon-50 tw-font-medium">
  
      ESC

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

          <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium">
  Close
</div>
        </div>
      </div>
    </div>
  </div>

  <div id="search-backdrop" class="tw-hidden 2lg:tw-hidden tw-h-screen tw-w-screen tw-fixed tw-left-0 tw-top-[3rem] tw-bg-white dark:tw-bg-moon-900" data-search-v2-target="searchBackdrop"></div>
</div>

    </div>
  </div>
  <div data-view-component="true" class="tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
</div>


</header>

    <div
      class="tw-flex container tw-justify-center tw-items-center tw-mt-2 tw-h-50px md:tw-h-100px"
      data-ads-target="banner"
    >
      <!-- /8691100/CoinGecko_leaderboard_728x90_atf_ROS -->
      <div data-aaad="true" data-aa-adunit="/22743369056/CoinGecko_S2S_Leaderboard_ATF_ROS"></div>
    </div>


<!-- START: Page Content -->
<div class="container">
  <div class="gecko-flash-container"></div>

  <main>
    
<script type="application/ld+json">
  {
    "@context": "https://schema.org/",
    "@type": "BreadcrumbList",
    "itemListElement": [{
      "@type": "ListItem",
      "position": 1,
      "name": "Cryptocurrencies",
      "item": "https://www.coingecko.com/"
    },{
      "@type": "ListItem",
      "position": 2,
      "name": "Crypto Exchanges",
      "item": "https://www.coingecko.com/en/exchanges"
    },{
      "@type": "ListItem",
      "position": 3,
      "name": "XT.COM"
    }]
  }
</script>




<nav class="tw-flex tw-truncate" aria-label="Breadcrumbs" data-view-component="true"><ol role="list" class="tw-flex tw-items-center tw-space-x-4 tw-list-none"><li><a href="/"><span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 hover:tw-text-primary-500 dark:hover:tw-text-primary-400 tw-font-medium tw-text-sm tw-leading-5">
  Cryptocurrencies
</span></a><i data-view-component="true" class="tw-ml-4 far fa-angle-right tw-text-gray-400 dark:tw-text-moon-100"></i>
</li><li><a href="/en/exchanges"><span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 hover:tw-text-primary-500 dark:hover:tw-text-primary-400 tw-font-medium tw-text-sm tw-leading-5">
  Crypto Exchanges
</span></a><i data-view-component="true" class="tw-ml-4 far fa-angle-right tw-text-gray-400 dark:tw-text-moon-100"></i>
</li><li><span aria-current="page" data-view-component="true" class="tw-text-gray-400 dark:tw-text-moon-300 tw-font-medium tw-text-sm tw-leading-5">
  XT.COM
</span></li></ol></nav>

<!-- TODO: Alerts -->
<div data-controller="exchange-show" data-market-type="spot" class="tw-mb-8">


  <div class="tw-mt-6 tw-mb-4 md:tw-mb-6 tw-flex tw-flex-col lg:tw-flex-row tw-justify-between lg:tw-items-center tw-gap-y-3">
    <div class="tw-flex tw-flex-col lg:tw-flex-row lg:tw-items-center tw-gap-2">
      <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-view-component="true" class="lg:tw-order-1 tw-w-fit tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-gray-100 dark:tw-bg-moon-400/20 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-700 dark:tw-text-moon-200 tw-font-medium">
  
      Centralized Exchange

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

      <span class="tw-flex tw-items-center">
        <img class="tw-rounded tw-h-10 tw-w-10 tw-mr-2" src="https://assets.coingecko.com/markets/images/404/large/20240701-155217.jpeg?1719895821" />
        <h1 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-2xl md:tw-text-3xl tw-leading-9">
  XT.COM
</h1>
      </span>
    </div>

    <div class="tw-flex tw-flex-col lg:tw-flex-row lg:tw-items-center tw-gap-x-2 tw-gap-y-3">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a href="https://www.xt.com/register?ref=ZHOJUG5" rel="nofollow noopener" target="_blank" role="button" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold">
  
      
          Start Trading
          <i data-view-component="true" class="fas fa-external-link tw-ml-0.5"></i>



</div></a>        <div onclick="Modal.info(&#39;🥰  Support CoinGecko&#39;, &#39;&lt;div class=&quot;gecko-override-links undecorated&quot;&gt; Links on this page may contain affiliate links. CoinGecko may be compensated when you sign up and trade on these affiliate platforms. &lt;br/&gt;&lt;br/&gt; For more details, please refer to Clause 12.2 of our &lt;a href=&quot;https://www.coingecko.com/en/privacy&quot;&gt;privacy policy&lt;/a&gt; and Clause 5.2 in our &lt;a href=&quot;https://www.coingecko.com/en/terms&quot;&gt;terms of use&lt;/a&gt;. &lt;/div&gt;&#39;)" data-view-component="true" class="tw-cursor-pointer tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  Affiliate disclosures
</div>
      </div>

        <div x-data="{ activeButton: &#39;&#39; }" x-init="activeButton = &#39;spotItem&#39;" role="group" data-view-component="true" class="lg:-tw-order-1 tw-p-1 tw-bg-gray-100 dark:tw-bg-moon-800 tw-rounded-lg tw-w-fit tw-isolate">
    <button data-key="spot" label="Spot" data-exchange-show-target="tickerTypeItem" data-action="click-&gt;exchange-show#handleTickerType" id="spotItem" @click="activeButton = &#39;spotItem&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;spotItem&#39; }" type="button" data-view-component="true" class="gecko-button-group-item selected">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    Spot

</span></button>
    <a data-key="perpetuals" label="Perpetuals" href="/en/exchanges/xt-derivatives" data-exchange-show-target="tickerTypeItem" data-action="click-&gt;exchange-show#handleTickerType" id="perpetualsItem" @click="activeButton = &#39;perpetualsItem&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;perpetualsItem&#39; }" role="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    Perpetuals

</span></a>
    <a data-key="futures" label="Futures" href="/en/exchanges/xt-derivatives#futures" data-exchange-show-target="tickerTypeItem" data-action="click-&gt;exchange-show#handleTickerType" id="futuresItem" @click="activeButton = &#39;futuresItem&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;futuresItem&#39; }" role="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    Futures

</span></a>
</div>    </div>
  </div>

  <div class="tw-mb-4 md:tw-mb-6 tw-flex tw-flex-col lg:tw-flex-row tw-gap-2">
      <div data-view-component="true" class="tw-flex-1 tw-overflow-hidden tw-flex tw-items-center tw-justify-between tw-gap-3 tw-rounded-xl tw-bg-white tw-p-4 tw-ring-2 tw-h-full tw-ring-gray-200 dark:tw-bg-moon-900 dark:tw-ring-moon-700">
  <div class="tw-flex tw-flex-col">
    <div data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg tw-leading-7">
  <span data-price-target="price" data-price-btc="16314.0840492194075511">BTC16,314.0840</span>
</div>
    <div data-view-component="true" class="tw-mt-1 tw-flex tw-flex-wrap tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold tw-text-sm tw-leading-5">
            24h Trading Volume
          <span class="gecko-up"><i class="fas fa-fw fa-caret-up"></i>8.9%</span>

</div>
  </div>
</div>

        <div class="tw-grid tw-grid-cols-2 tw-gap-2 tw-grow-[2] tw-h-fit">
          <div data-view-component="true" class="tw-flex-1 !tw-h-fit tw-overflow-hidden tw-flex tw-items-center tw-justify-between tw-gap-3 tw-rounded-xl tw-bg-white tw-p-4 tw-ring-2 tw-h-full tw-ring-gray-200 dark:tw-bg-moon-900 dark:tw-ring-moon-700">
  <div class="tw-flex tw-flex-col">
    <div data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg tw-leading-7">
  893
</div>
    <div data-view-component="true" class="tw-mt-1 tw-flex tw-flex-wrap tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold tw-text-sm tw-leading-5">
  Coins
</div>
  </div>
</div>
          <div data-view-component="true" class="tw-flex-1 !tw-h-fit tw-overflow-hidden tw-flex tw-items-center tw-justify-between tw-gap-3 tw-rounded-xl tw-bg-white tw-p-4 tw-ring-2 tw-h-full tw-ring-gray-200 dark:tw-bg-moon-900 dark:tw-ring-moon-700">
  <div class="tw-flex tw-flex-col">
    <div data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg tw-leading-7">
  1,016
</div>
    <div data-view-component="true" class="tw-mt-1 tw-flex tw-flex-wrap tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold tw-text-sm tw-leading-5">
  Pairs
</div>
  </div>
</div>        </div>

        <div data-view-component="true" class="tw-flex-1 tw-overflow-hidden tw-flex tw-items-center tw-justify-between tw-gap-3 tw-rounded-xl tw-bg-white tw-p-4 tw-ring-2 tw-h-full tw-ring-gray-200 dark:tw-bg-moon-900 dark:tw-ring-moon-700">
  <div class="tw-flex tw-flex-col">
    <div data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg tw-leading-7">
  <div class="tw-text-success-500 dark:tw-text-success-400">8/10</div>
</div>
    <div data-view-component="true" class="tw-mt-1 tw-flex tw-flex-wrap tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold tw-text-sm tw-leading-5">
              Trust Score
            <div data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle tw-ml-1"></i>

  </div>
  <div>
    <div role="tooltip" class="tw-max-w-sm tw-font-normal gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Trust Score is a rating algorithm developed by CoinGecko to evaluate the legitimacy of an exchange’s trading volume. Trust Score is calculated on a range of metrics such as liquidity, scale of operations, cybersecurity score, and more. For more details read our <a href="https://www.coingecko.com/en/methodology" target="_blank">full methodology</a>.
      <div data-popper-arrow></div>
    </div>
  </div>
</div>
</div>
  </div>
</div>  </div>
  <div>
    <div class="tw-sticky tw-top-0 tw-mb-4 tw-z-20" data-exchange-show-target="exchangeTabs">
      <div x-data="{ activeTab: &#39;&#39; }" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-900">
  <nav class="tw-overflow-x-auto tw-flex tw-shadow-[inset_0_-1px_0_0_#EFF2F5] dark:tw-shadow-[inset_0_-1px_0_0_#212D3B]">
      <a data-action="click-&gt;exchange-show#scrollToAnchor" id="tab-markets" data-view-component="true" class="selected gecko-tab-underline-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    Markets
    

</span></a>

      <a data-action="click-&gt;exchange-show#scrollToAnchor" id="tab-about" data-view-component="true" class="gecko-tab-underline-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    About
    

</span></a>

      <a data-action="click-&gt;exchange-show#scrollToAnchor" id="tab-statistics" data-view-component="true" class="gecko-tab-underline-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    Statistics
    

</span></a>

      <a data-action="click-&gt;exchange-show#scrollToAnchor" id="tab-trust-score" data-view-component="true" class="gecko-tab-underline-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    Trust Score
    

</span></a>

      <a label="Exchange Token" href="/en/coins/xtcom-token" external="true" target="_blank" id="tab-nav-link-0" data-view-component="true" class="gecko-tab-underline-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <span data-view-component="true">Exchange Token</span>
    <span data-view-component="true" class="tw--mr-0.5 tw-ml-1"><i data-view-component="true" class="fas fa-external-link"></i>
</span>

</span></a>

  </nav>

  <div data-view-component="true"></div></div>    </div>

    <span data-exchange-show-target="navAnchor" data-key="tab-markets"></span>
      <div data-exchange-show-target="spotTable" data-controller="more-content" data-page-size="50"
     data-content-count="892">
  <div class="tw-mb-3 tw-flex tw-justify-between tw-items-center">
    <h2 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-xl md:tw-text-2xl tw-leading-8">
  Spot Markets
</h2>
    <div x-data="{open: false}" data-view-component="true" class="tw-inline-block tw-text-left">
  <div @click="open = !open">
    <button :class="open &amp;&amp; &#39;gecko-button-dropdown-soft gecko-button-dropdown-open&#39;" type="button" data-view-component="true" class="pair-targets-button tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      All Pairs

</div>    <i :class="{&#39;tw-rotate-180&#39;: open}" data-view-component="true" class="tw-ml-2 tw-transform tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 fas fa-chevron-down"></i>

</button>
  </div>

  <div class="tw-z-[2000]" x-data="popperable(&#39;open&#39;)" data-placement="bottom-end" x-cloak="true">
  <div @click.away="open = false" x-show="open" x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" style="; display: none" data-view-component="true" class="tw-min-w-fit tw-max-h-[20rem] tw-overflow-y-auto dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true">
  
            <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            All Pairs

  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-check tw-text-success-500 dark:tw-text-success-400"></i>

</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=BNB&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            BNB

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=BTC&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            BTC

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=DAI&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            DAI

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=DOGE&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            DOGE

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=ETH&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            ETH

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=INR&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            INR

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=USDC&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            USDC

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=USDT&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            USDT

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=XT&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            XT

  
</span>          <span @click="open = false" data-action="click-&gt;exchange-show#reloadMarkets" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?target=XTUSD&amp;type=spot" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
            XTUSD

  
</span>
</div>

</div></div></div>  </div>

  <div class="tw-relative">
    <div class="!tw-hidden tw-bg-white/90 dark:tw-bg-moon-900/90 tw-absolute tw-w-full tw-h-full tw-flex tw-items-center tw-justify-center tw-z-[1] markets-loading">
      <i class="far fa-spin fa-spinner-third tw-text-2xl dark:tw-text-moon-50"></i>
    </div>

    <div class="tw-w-full tw-overflow-x-auto">
        <div class="">
  <table data-view-component="true" class="tw-border-y tw-border-gray-200 dark:tw-border-moon-700 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;tbody:first-of-type]:!tw-border-t-0 tw-w-full sortable">
      <thead class="">
        <tr>
            <th aria-sort="ascending" data-view-component="true" class="tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  #
</th>
            <th data-view-component="true" class="tw-min-w-[220px] tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Coin
</th>
            <th data-view-component="true" class="tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Pair
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Price
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Spread
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  +2% Depth
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  -2% Depth
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  24h Volume
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Volume %
</th>
            <th data-view-component="true" class="tw-text-end indicator-left tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Last Updated
</th>
            <th data-view-component="true" class="tw-text-center indicator-left no-sort tw-py-3 tw-px-1 2lg:tw-pl-2.5 tw-font-semibold tw-text-xs tw-text-gray-900 dark:tw-text-moon-50 tw-whitespace-nowrap tw-text-left tw-bg-white dark:tw-bg-moon-900">
  Trust Score
</th>
        </tr>
        <tr>
          <th class="tw-p-0 tw-h-px tw-bg-gray-200 dark:tw-bg-moon-700 no-sort" colspan="11"></th>
        </tr>
      </thead>

    

          <tbody data-more-content-target="content" data-view-component="true" class="tw-divide-y tw-divide-gray-200 tw-min-w-full dark:tw-divide-moon-700">
    
            <tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  1
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/bitcoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Bitcoin" src="https://assets.coingecko.com/coins/images/1/standard/bitcoin.png?1696501400" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Bitcoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/btc_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  BTC/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="65715.0095727629203699719317375011872" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="1.000606725484063331112">$65,715.01</span>
</td>
      <td data-sort="0.011005" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.01%
</td>
      <td data-sort="8840866.630057" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $8,840,867
</td>
      <td data-sort="9150458.058462141" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $9,150,458
</td>
      <td data-sort="5184.488260025771803204126091" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="5184.488260025771803204126091">$340,492,110</span>
</td>
      <td data-sort="31.78" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  31.78%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  2
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/ethereum">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Ethereum" src="https://assets.coingecko.com/coins/images/279/standard/ethereum.png?1696501628" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Ethereum
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/eth_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  ETH/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2661.57875397898426538545255445436" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0405264127472741931">$2,661.58</span>
</td>
      <td data-sort="0.010752" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.01%
</td>
      <td data-sort="994714.091017581" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $994,714
</td>
      <td data-sort="989077.3040648709" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $989,077
</td>
      <td data-sort="1915.67003840401550441222959" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="1915.67003840401550441222959">$125,811,941</span>
</td>
      <td data-sort="11.74" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  11.74%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  3
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/neiro-3">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Neiro" src="https://assets.coingecko.com/coins/images/39488/standard/logo.png?1723247657" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Neiro
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/neiro_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  NEIRO/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.0010583397454964009998589167955708684" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000000016112485392749419516">$0.0010583397454964010000000000000000000</span>
</td>
      <td data-sort="0.100121" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.1%
</td>
      <td data-sort="138591.61365250216" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $138,592
</td>
      <td data-sort="141840.60435186984" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $141,841
</td>
      <td data-sort="876.8726121328741329259" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="876.8726121328741329259">$57,596,895</span>
</td>
      <td data-sort="5.37" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  5.37%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  4
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/xtcom-token">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="XT.com" src="https://assets.coingecko.com/coins/images/8391/standard/20240701-155217.jpeg?1719895785" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  XT.com
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/xt_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  XT/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="5.168823948491994358599174432789852" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00007870287228639190067">$5.17</span>
</td>
      <td data-sort="0.011609" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.01%
</td>
      <td data-sort="291865.29164292855" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $291,865
</td>
      <td data-sort="278585.4502387658" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $278,585
</td>
      <td data-sort="288.759030797603535578531" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="288.759030797603535578531">$18,964,296</span>
</td>
      <td data-sort="1.77" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  1.77%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  5
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/ethereum">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Ethereum" src="https://assets.coingecko.com/coins/images/279/standard/ethereum.png?1696501628" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Ethereum
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/eth_usdc?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  ETH/USDC<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2661.334479832557166550084758521078" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.040522693317643642755">$2,661.33</span>
</td>
      <td data-sort="0.020281" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.02%
</td>
      <td data-sort="165133.61223896328" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $165,134
</td>
      <td data-sort="152105.4653039049" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $152,105
</td>
      <td data-sort="227.0290204286032530141771" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="227.0290204286032530141771">$14,910,167</span>
</td>
      <td data-sort="1.39" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  1.39%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  6
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/dogecoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Dogecoin" src="https://assets.coingecko.com/coins/images/5/standard/dogecoin.png?1696501409" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Dogecoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/doge_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  DOGE/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.1196360145672402510269650432312236" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000001821632554942302231">$0.1196360145672402500000000000000000</span>
</td>
      <td data-sort="0.016717" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.02%
</td>
      <td data-sort="3042556.5245191436" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $3,042,557
</td>
      <td data-sort="3007214.911410835" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $3,007,215
</td>
      <td data-sort="191.2295668663752143442" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="191.2295668663752143442">$12,559,032</span>
</td>
      <td data-sort="1.17" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  1.17%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  7
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/sei">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Sei" src="https://assets.coingecko.com/coins/images/28205/standard/Sei_Logo_-_Transparent.png?1696527207" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Sei
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/sei_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  SEI/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.492707137997011517898862806585576" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000750218373517747746">$0.492707137997011500000000000000000</span>
</td>
      <td data-sort="0.040609" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.04%
</td>
      <td data-sort="151606.0238955531" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $151,606
</td>
      <td data-sort="150756.30224486665" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $150,756
</td>
      <td data-sort="177.7144574933163715048" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="177.7144574933163715048">$11,671,425</span>
</td>
      <td data-sort="1.09" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  1.09%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  8
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/solana">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Solana" src="https://assets.coingecko.com/coins/images/4128/standard/solana.png?1718769756" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Solana
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/sol_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  SOL/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="157.7543032985965420280321596725072" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.002402039014844075812">$157.75</span>
</td>
      <td data-sort="0.02536" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="394531.20560139767" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $394,531
</td>
      <td data-sort="406123.2661737867" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $406,123
</td>
      <td data-sort="160.8167061015152069804682" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="160.8167061015152069804682">$10,561,663</span>
</td>
      <td data-sort="0.99" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.99%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  9
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/hamster-kombat">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Hamster Kombat" src="https://assets.coingecko.com/coins/images/39102/standard/hamster-removebg-preview.png?1720514486" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Hamster Kombat
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/hmstr_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  HMSTR/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.00711655350813017194695105115854206" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000001083445698174027094">$0.00711655350813017200000000000000000</span>
</td>
      <td data-sort="0.028149" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="20597.84764389477" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $20,598
</td>
      <td data-sort="22145.223977730973" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $22,145
</td>
      <td data-sort="154.419989821741125487241" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="154.419989821741125487241">$10,142,992</span>
</td>
      <td data-sort="0.95" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.95%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  10
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/bnb">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="BNB" src="https://assets.coingecko.com/coins/images/825/standard/bnb-icon2_2x.png?1696501970" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  BNB
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/bnb_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  BNB/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="608.832389157086705125939485117012" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00927035980430883177">$608.83</span>
</td>
      <td data-sort="0.032852" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="409761.9772947503" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $409,762
</td>
      <td data-sort="412767.7794194624" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $412,768
</td>
      <td data-sort="145.0055729208679209921374" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="145.0055729208679209921374">$9,523,264</span>
</td>
      <td data-sort="0.89" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.89%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  11
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/simons-cat">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Simon&#39;s Cat" src="https://assets.coingecko.com/coins/images/39765/standard/Simon&#39;s_Cat_Logo.png?1724017505" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Simon&#39;s Cat
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/cat_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  CAT/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.000044716044674363042736675848578413" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000000068077063126762737">$0.000044716044674363040000000000000000</span>
</td>
      <td data-sort="0.089445" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.09%
</td>
      <td data-sort="71648.14407282215" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $71,648
</td>
      <td data-sort="79837.93719503167" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $79,838
</td>
      <td data-sort="142.4543614654306378209" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="142.4543614654306378209">$9,357,036</span>
</td>
      <td data-sort="0.87" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.87%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  12
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/aave">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Aave" src="https://assets.coingecko.com/coins/images/12645/standard/aave-token-round.png?1720472354" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Aave
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/aave_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  AAVE/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="167.836495647378263709762848041128" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00255555507666013138">$167.84</span>
</td>
      <td data-sort="0.107213" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.11%
</td>
      <td data-sort="251058.97114442955" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $251,059
</td>
      <td data-sort="276062.34827947355" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $276,062
</td>
      <td data-sort="106.2311942877311805933829" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="106.2311942877311805933829">$6,976,750</span>
</td>
      <td data-sort="0.65" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.65%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  13
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/injective">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Injective" src="https://assets.coingecko.com/coins/images/12882/standard/Secondary_Symbol.png?1696512670" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Injective
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/inj_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  INJ/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="23.4651024307955546283136854293496" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000357290358155224566">$23.47</span>
</td>
      <td data-sort="0.255537" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.26%
</td>
      <td data-sort="62399.89110272388" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $62,400
</td>
      <td data-sort="64898.10288383473" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $64,898
</td>
      <td data-sort="106.079347576019462293921" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="106.079347576019462293921">$6,966,778</span>
</td>
      <td data-sort="0.65" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.65%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  14
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/dogwifhat">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="dogwifhat" src="https://assets.coingecko.com/coins/images/33566/standard/dogwifhat.jpg?1702499428" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  dogwifhat
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/wif_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  WIF/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2.24680618207202223683610639613234" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000342060590117917466">$2.25</span>
</td>
      <td data-sort="0.089008" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.09%
</td>
      <td data-sort="102517.19385024266" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $102,517
</td>
      <td data-sort="114562.71798006183" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $114,563
</td>
      <td data-sort="101.274436173424309225409" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="101.274436173424309225409">$6,652,155</span>
</td>
      <td data-sort="0.62" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.62%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  15
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/constitutiondao">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="ConstitutionDAO" src="https://assets.coingecko.com/coins/images/20612/standard/GN_UVm3d_400x400.jpg?1696520017" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  ConstitutionDAO
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/people_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  PEOPLE/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.0740761076736879273560490853750056" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000001127916620842963826">$0.0740761076736879300000000000000000</span>
</td>
      <td data-sort="0.027001" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="556502.6899878103" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $556,503
</td>
      <td data-sort="584698.683947707" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $584,699
</td>
      <td data-sort="100.68768514445587387962" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="100.68768514445587387962">$6,612,680</span>
</td>
      <td data-sort="0.62" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.62%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  16
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/starknet">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Starknet" src="https://assets.coingecko.com/coins/images/26433/standard/starknet.png?1696525507" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Starknet
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/strk_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  STRK/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.478571717499223258282454719461136" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000728592102904771664">$0.478571717499223300000000000000000</span>
</td>
      <td data-sort="0.041797" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.04%
</td>
      <td data-sort="266217.35135899845" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $266,217
</td>
      <td data-sort="239793.1445540034" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $239,793
</td>
      <td data-sort="100.190686945973298600906" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="100.190686945973298600906">$6,580,970</span>
</td>
      <td data-sort="0.61" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.61%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  17
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/stacks">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Stacks" src="https://assets.coingecko.com/coins/images/2069/standard/Stacks_Logo_png.png?1709979332" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Stacks
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/stx_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  STX/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2.07145043197687952409367615192596" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000315408496052630041">$2.07</span>
</td>
      <td data-sort="0.192957" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.19%
</td>
      <td data-sort="29002.11238270942" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $29,002
</td>
      <td data-sort="33200.44928067508" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $33,200
</td>
      <td data-sort="99.43463922644159118931" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="99.43463922644159118931">$6,530,386</span>
</td>
      <td data-sort="0.61" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.61%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  18
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/bittensor">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Bittensor" src="https://assets.coingecko.com/coins/images/28452/standard/ARUsPeNQ_400x400.jpeg?1696527447" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Bittensor
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/tao_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  TAO/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="538.19311039837398193135585089902" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0081936152040712198">$538.19</span>
</td>
      <td data-sort="0.111794" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.11%
</td>
      <td data-sort="47506.48661734349" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $47,506
</td>
      <td data-sort="43846.15009354229" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $43,846
</td>
      <td data-sort="96.70618265384152775066063" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="96.70618265384152775066063">$6,352,092</span>
</td>
      <td data-sort="0.59" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.59%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  19
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/xrp">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="XRP" src="https://assets.coingecko.com/coins/images/44/standard/xrp-symbol-white-128.png?1696501442" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  XRP
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/xrp_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  XRP/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.595829561723142024385612208451132" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000907237281982383947">$0.595829561723142000000000000000000</span>
</td>
      <td data-sort="0.033568" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="159982.08793625108" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $159,982
</td>
      <td data-sort="169017.63201122227" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $169,018
</td>
      <td data-sort="91.4705655632518602698" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="91.4705655632518602698">$6,007,344</span>
</td>
      <td data-sort="0.56" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.56%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  20
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/moo-deng">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Moo Deng" src="https://assets.coingecko.com/coins/images/50264/standard/MOODENG.jpg?1726726975" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Moo Deng
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/moodeng_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  MOODENG/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.144651902906328769121327241710034" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000220222445819460666">$0.144651902906328760000000000000000</span>
</td>
      <td data-sort="0.303825" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.3%
</td>
      <td data-sort="18794.880567899672" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $18,795
</td>
      <td data-sort="20767.762565223413" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $20,768
</td>
      <td data-sort="91.310001621681180095133" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="91.310001621681180095133">$5,997,647</span>
</td>
      <td data-sort="0.56" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.56%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  21
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/fantom">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Fantom" src="https://assets.coingecko.com/coins/images/4001/standard/Fantom_round.png?1696504642" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Fantom
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/ftm_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  FTM/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.72565779256360506746980301700738" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00001104919671106630105">$0.72565779256360510000000000000000</span>
</td>
      <td data-sort="0.110208" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.11%
</td>
      <td data-sort="385297.1030061367" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $385,297
</td>
      <td data-sort="327746.91508331307" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $327,747
</td>
      <td data-sort="90.7436487348311923868" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="90.7436487348311923868">$5,959,603</span>
</td>
      <td data-sort="0.56" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.56%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  22
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/near">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="NEAR Protocol" src="https://assets.coingecko.com/coins/images/10365/standard/near.jpg?1696510367" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  NEAR Protocol
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/near_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  NEAR/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="5.78325755562062646465940874477832" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000880585187917096522">$5.78</span>
</td>
      <td data-sort="0.069144" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.07%
</td>
      <td data-sort="143825.8011035064" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $143,826
</td>
      <td data-sort="141512.94200721517" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $141,513
</td>
      <td data-sort="80.71806910118116121916" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="80.71806910118116121916">$5,301,172</span>
</td>
      <td data-sort="0.49" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.49%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  23
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/worldcoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Worldcoin" src="https://assets.coingecko.com/coins/images/31069/standard/worldcoin.jpeg?1696529903" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Worldcoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/wld_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  WLD/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2.15146783157038525172645939294676" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000327592310482475721">$2.15</span>
</td>
      <td data-sort="0.09298" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.09%
</td>
      <td data-sort="44282.92307298101" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $44,283
</td>
      <td data-sort="45255.53881515338" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $45,256
</td>
      <td data-sort="72.44799893858585604645" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="72.44799893858585604645">$4,758,034</span>
</td>
      <td data-sort="0.44" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.44%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  24
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/arbitrum-iou-deactivated">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Arbitrum IOU" src="https://assets.coingecko.com/coins/images/29463/standard/arb.jpeg?1696528409" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Arbitrum IOU
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/arb_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  ARB/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.643439914481277932327118236858508" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000979730977839965743">$0.643439914481277900000000000000000</span>
</td>
      <td data-sort="0.031085" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="299314.2378694365" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $299,314
</td>
      <td data-sort="329275.8727015381" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $329,276
</td>
      <td data-sort="69.64381942169348998966" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="69.64381942169348998966">$4,573,869</span>
</td>
      <td data-sort="0.43" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.43%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  25
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/bonfida">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Bonfida" src="https://assets.coingecko.com/coins/images/13395/standard/bonfida.png?1696513157" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Bonfida
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/fida_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  FIDA/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.342674513759188278587394229671576" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000521771852958141246">$0.342674513759188300000000000000000</span>
</td>
      <td data-sort="0.116686" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.12%
</td>
      <td data-sort="21663.60554882549" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $21,664
</td>
      <td data-sort="12721.696257797352" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $12,722
</td>
      <td data-sort="68.47645465568029331324" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="68.47645465568029331324">$4,497,202</span>
</td>
      <td data-sort="0.42" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.42%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  26
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/saga">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Saga" src="https://assets.coingecko.com/coins/images/25691/standard/zcPXETKs_400x400.jpg?1696524818" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Saga
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/saga_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  SAGA/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2.514102091176939575074132945129028" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00003827545303136020372">$2.51</span>
</td>
      <td data-sort="0.047716" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.05%
</td>
      <td data-sort="265245.0265868784" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $265,245
</td>
      <td data-sort="249891.87318191712" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $249,892
</td>
      <td data-sort="62.04126694621974754853" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="62.04126694621974754853">$4,075,146</span>
</td>
      <td data-sort="0.38" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.38%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  27
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/chiliz">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Chiliz" src="https://assets.coingecko.com/coins/images/8834/standard/CHZ_Token_updated.png?1696508986" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Chiliz
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/chz_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  CHZ/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.069915202894825629519144356841924" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000106456078580776629">$0.069915202894825630000000000000000</span>
</td>
      <td data-sort="0.285714" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.29%
</td>
      <td data-sort="14851.748769706179" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $14,852
</td>
      <td data-sort="14357.165632480212" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $14,357
</td>
      <td data-sort="59.5096789555199263518" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="59.5096789555199263518">$3,908,307</span>
</td>
      <td data-sort="0.36" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.36%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  28
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/tron">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="TRON" src="https://assets.coingecko.com/coins/images/1094/standard/tron-logo.png?1696502193" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  TRON
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/trx_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  TRX/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.153133298472071586257238927503556" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000233167748651171701">$0.153133298472071580000000000000000</span>
</td>
      <td data-sort="0.130548" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.13%
</td>
      <td data-sort="2450808.143170689" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $2,450,808
</td>
      <td data-sort="331231.109742939" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $331,231
</td>
      <td data-sort="59.30171190404008670917" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="59.30171190404008670917">$3,894,649</span>
</td>
      <td data-sort="0.36" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.36%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  29
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/chainlink">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Chainlink" src="https://assets.coingecko.com/coins/images/877/standard/chainlink-new-logo.png?1696502009" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Chainlink
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/link_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  LINK/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="12.7227665353674106936125353223072" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000193722649434546312">$12.72</span>
</td>
      <td data-sort="0.157109" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.16%
</td>
      <td data-sort="56496.42593476243" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $56,496
</td>
      <td data-sort="66094.52027137068" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $66,095
</td>
      <td data-sort="56.698546897220849230789" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="56.698546897220849230789">$3,723,686</span>
</td>
      <td data-sort="0.35" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.35%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  30
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/mother-iggy">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Mother Iggy" src="https://assets.coingecko.com/coins/images/38269/standard/mother.png?1716954537" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Mother Iggy
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/mother_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  MOTHER/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.141350718400167739120633051546527" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000215196622367149323">$0.141350718400167750000000000000000</span>
</td>
      <td data-sort="0.212089" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.21%
</td>
      <td data-sort="9052.322537800763" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $9,052
</td>
      <td data-sort="9893.025474200555" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $9,893
</td>
      <td data-sort="56.028691440705559859359" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="56.028691440705559859359">$3,680,213</span>
</td>
      <td data-sort="0.34" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.34%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  31
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/avalanche">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Avalanche" src="https://assets.coingecko.com/coins/images/12559/standard/Avalanche_Circle_RedWhite_Trans.png?1696512369" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Avalanche
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/avax_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  AVAX/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="29.3663856508166020412314494546336" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000447145989575336456">$29.37</span>
</td>
      <td data-sort="0.136147" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.14%
</td>
      <td data-sort="71548.16475590342" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $71,548
</td>
      <td data-sort="76188.23355216953" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $76,188
</td>
      <td data-sort="54.323646567530852805634" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="54.323646567530852805634">$3,567,714</span>
</td>
      <td data-sort="0.33" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.33%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  32
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/phoenix">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Phoenix" src="https://assets.coingecko.com/coins/images/20052/standard/Phoenix_logo_blue_bird.png?1696519471" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Phoenix
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/phb_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  PHB/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="1.72237452625021078729565926297272" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000262256605602428262">$1.72</span>
</td>
      <td data-sort="0.116009" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.12%
</td>
      <td data-sort="52990.630834823045" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $52,991
</td>
      <td data-sort="47007.59995868581" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $47,008
</td>
      <td data-sort="54.28477806733211986344" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="54.28477806733211986344">$3,565,161</span>
</td>
      <td data-sort="0.33" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.33%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  33
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/ethereum">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Ethereum" src="https://assets.coingecko.com/coins/images/279/standard/ethereum.png?1696501628" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Ethereum
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/eth_xtusd?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  ETH/XTUSD<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="2674.40611318406927437736786213078045028" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0407217279724298139364413">$2,674.41</span>
</td>
      <td data-sort="0.995211" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  1.0%
</td>
      <td data-sort="39179.45047940403" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $39,179
</td>
      <td data-sort="46083.498541402" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $46,083
</td>
      <td data-sort="52.557393899698457741357091" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="52.557393899698457741357091">$3,451,715</span>
</td>
      <td data-sort="0.32" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.32%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  34
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/edelcoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Edelcoin" src="https://assets.coingecko.com/coins/images/31621/standard/edelcoin_logo_200_%281%29.png?1696530437" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Edelcoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/edlc_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  EDLC/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="1.125944834030117469952801180213932" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00001714414987959660247">$1.13</span>
</td>
      <td data-sort="0.443459" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.44%
</td>
      <td data-sort="49371.61172367759" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $49,372
</td>
      <td data-sort="16822.004879054024" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $16,822
</td>
      <td data-sort="50.068353125773253284762" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="50.068353125773253284762">$3,288,247</span>
</td>
      <td data-sort="0.31" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.31%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  35
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/artificial-superintelligence-alliance">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Artificial Superintelligence Alliance" src="https://assets.coingecko.com/coins/images/5681/standard/ASI.png?1719827289" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Artificial Superintelligence Alliance
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/fet_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  FET/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="1.67860230343582070944389427101962" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000255555507666013138">$1.68</span>
</td>
      <td data-sort="0.118977" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.12%
</td>
      <td data-sort="41590.819613046195" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $41,591
</td>
      <td data-sort="40166.05321639152" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $40,166
</td>
      <td data-sort="50.01986276272391046293" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="50.01986276272391046293">$3,285,527</span>
</td>
      <td data-sort="0.31" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.31%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  36
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/usdc">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="USDC" src="https://assets.coingecko.com/coins/images/6319/standard/usdc.png?1696506694" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  USDC
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/usdc_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  USDC/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="1.000017451419837831090708554657448" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00001522672208369963858">$1.00</span>
</td>
      <td data-sort="0.04" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.04%
</td>
      <td data-sort="3254722.1553268917" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $3,254,722
</td>
      <td data-sort="3325598.738881095" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $3,325,599
</td>
      <td data-sort="49.4231711118598443999" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="49.4231711118598443999">$3,245,874</span>
</td>
      <td data-sort="0.3" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.3%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-warning-600"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  37
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/litecoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Litecoin" src="https://assets.coingecko.com/coins/images/2/standard/litecoin.png?1696501400" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Litecoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/ltc_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  LTC/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="68.314854902955514966488692021508" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00104019315694807493">$68.31</span>
</td>
      <td data-sort="0.02927" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="411644.3264117847" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $411,644
</td>
      <td data-sort="437728.75143350725" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $437,729
</td>
      <td data-sort="48.8240735383900847477475" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="48.8240735383900847477475">$3,206,528</span>
</td>
      <td data-sort="0.3" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.3%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  38
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/cardano">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Cardano" src="https://assets.coingecko.com/coins/images/975/standard/cardano.png?1696502090" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Cardano
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/ada_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  ADA/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.402687563454317574311981660437176" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000613150461181983846">$0.402687563454317550000000000000000</span>
</td>
      <td data-sort="0.049665" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.05%
</td>
      <td data-sort="398237.88908045" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $398,238
</td>
      <td data-sort="405344.42059875233" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $405,344
</td>
      <td data-sort="47.89615689662244428769" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="47.89615689662244428769">$3,145,587</span>
</td>
      <td data-sort="0.29" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.29%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  39
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/floki">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="FLOKI" src="https://assets.coingecko.com/coins/images/16746/standard/PNG_image.png?1696516318" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  FLOKI
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/floki_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  FLOKI/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.0001522731114264413996851865076625824" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000000002318579885999632904">$0.0001522731114264414000000000000000000</span>
</td>
      <td data-sort="0.209905" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.21%
</td>
      <td data-sort="263885.928485672" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $263,886
</td>
      <td data-sort="261759.3255438456" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $261,759
</td>
      <td data-sort="47.6340236521411182132" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="47.6340236521411182132">$3,128,372</span>
</td>
      <td data-sort="0.29" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.29%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  40
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/mog-coin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Mog Coin" src="https://assets.coingecko.com/coins/images/31059/standard/MOG_LOGO_200x200.png?1696529893" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Mog Coin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/mog_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  MOG/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.00000149953805295011635486078516821121" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000000000228294222879233429">$0.0<sub title="0.00000149953805295011635486078516821121">5</sub>149953805295011635486078516821121</span>
</td>
      <td data-sort="0.0666" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.07%
</td>
      <td data-sort="127281.63240325356" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $127,282
</td>
      <td data-sort="128848.95004354115" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $128,849
</td>
      <td data-sort="47.3396170062119346631" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="47.3396170062119346631">$3,109,476</span>
</td>
      <td data-sort="0.29" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.29%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-warning-600"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  41
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/arweave">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Arweave" src="https://assets.coingecko.com/coins/images/4343/standard/oRt6SiEN_400x400.jpg?1696504946" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Arweave
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/ar_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  AR/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="23.25505675686260209327762942167" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000354092106867390075">$23.26</span>
</td>
      <td data-sort="0.085985" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.09%
</td>
      <td data-sort="47215.07805457175" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $47,215
</td>
      <td data-sort="39552.94500591568" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $39,553
</td>
      <td data-sort="47.236030520524747437882" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="47.236030520524747437882">$3,102,233</span>
</td>
      <td data-sort="0.29" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.29%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  42
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/monero">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Monero" src="https://assets.coingecko.com/coins/images/69/standard/monero_logo.png?1696501460" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Monero
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/xmr_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  XMR/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="165.7260367330995501434481900592044" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.002523420266101413399">$165.73</span>
</td>
      <td data-sort="0.30135" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.3%
</td>
      <td data-sort="31295.502314267615" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $31,296
</td>
      <td data-sort="23635.561362852244" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $23,636
</td>
      <td data-sort="46.2233754646272983107316" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="46.2233754646272983107316">$3,035,727</span>
</td>
      <td data-sort="0.28" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.28%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  43
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/celo">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Celo" src="https://assets.coingecko.com/coins/images/11090/standard/InjXBNx9_400x400.jpg?1696511031" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Celo
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/celo_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  CELO/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.645731696583922686499424166831445" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000983081526808173305">$0.645731696583922700000000000000000</span>
</td>
      <td data-sort="0.185816" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.19%
</td>
      <td data-sort="18856.14310444848" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $18,856
</td>
      <td data-sort="24856.9326314584" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $24,857
</td>
      <td data-sort="45.4088631632823270606" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="45.4088631632823270606">$2,982,656</span>
</td>
      <td data-sort="0.28" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.28%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  44
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/notcoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Notcoin" src="https://assets.coingecko.com/coins/images/33453/standard/rFmThDiD_400x400.jpg?1701876350" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Notcoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/not_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  NOT/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.0087531407360330340927497466456625" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000000133260470326437125">$0.0087531407360330340000000000000000</span>
</td>
      <td data-sort="0.114286" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.11%
</td>
      <td data-sort="53150.44717347856" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $53,150
</td>
      <td data-sort="34032.58525889955" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $34,033
</td>
      <td data-sort="44.0846652919745493298" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="44.0846652919745493298">$2,895,677</span>
</td>
      <td data-sort="0.27" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.27%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  45
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/bonk">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Bonk" src="https://assets.coingecko.com/coins/images/28600/standard/bonk.jpg?1696527587" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Bonk
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/bonk_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  BONK/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.00002075451301956554810475315313977" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.000000000316017686774122325">$0.00002075451301956554800000000000000</span>
</td>
      <td data-sort="0.096154" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.1%
</td>
      <td data-sort="72356.58424928648" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $72,357
</td>
      <td data-sort="57995.12702108504" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $57,995
</td>
      <td data-sort="42.5403820427596466969" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="42.5403820427596466969">$2,793,846</span>
</td>
      <td data-sort="0.26" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.26%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  46
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/core">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Core" src="https://assets.coingecko.com/coins/images/28938/standard/file_589.jpg?1701868471" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Core
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/core_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  CORE/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="1.12224402929891783004978495531672" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000170877997378585662">$1.12</span>
</td>
      <td data-sort="0.382426" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.38%
</td>
      <td data-sort="57647.33400113845" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $57,647
</td>
      <td data-sort="67653.21437955699" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $67,653
</td>
      <td data-sort="42.258985426176332736975" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="42.258985426176332736975">$2,775,365</span>
</td>
      <td data-sort="0.26" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.26%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  47
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/neiro-on-eth">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Neiro on ETH" src="https://assets.coingecko.com/coins/images/39438/standard/Neiro.png?1722915026" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Neiro on ETH
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/neiroeth_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  NEIRO/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="0.092633237960761023655843033072954" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00000141027652025463746">$0.092633237960761020000000000000000</span>
</td>
      <td data-sort="0.215517" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.22%
</td>
      <td data-sort="22997.266811779067" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $22,997
</td>
      <td data-sort="21575.84577191065" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $21,576
</td>
      <td data-sort="40.190618292917545267224" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="40.190618292917545267224">$2,639,898</span>
</td>
      <td data-sort="0.25" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.25%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  48
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/popcat">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Popcat" src="https://assets.coingecko.com/coins/images/33760/standard/image.jpg?1702964227" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Popcat
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/popcat_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  POPCAT/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="1.083088625703196115682302936372433" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.00001648926985399239717">$1.08</span>
</td>
      <td data-sort="0.202821" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.2%
</td>
      <td data-sort="45231.28651590759" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $45,231
</td>
      <td data-sort="408631.83584599063" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $408,632
</td>
      <td data-sort="37.012118338952957472143" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="37.012118338952957472143">$2,431,120</span>
</td>
      <td data-sort="0.23" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.23%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  49
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/uniswap">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Uniswap" src="https://assets.coingecko.com/coins/images/12504/standard/uniswap-logo.png?1720676669" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Uniswap
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/uni_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  UNI/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="7.33759554272447522392622320160736" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0001117255783216848856">$7.34</span>
</td>
      <td data-sort="0.027259" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.03%
</td>
      <td data-sort="370932.1300300449" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $370,932
</td>
      <td data-sort="387960.6708601965" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $387,961
</td>
      <td data-sort="36.740554517507570095191" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="36.740554517507570095191">$2,412,941</span>
</td>
      <td data-sort="0.23" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.23%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr><tr data-view-component="true" class="hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm">
      <td data-view-component="true" class="tw-pl-2.5 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  50
</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
      <div class="tw-flex tw-items-center tw-gap-x-2">
        <a class="tw-flex tw-items-center tw-whitespace-nowrap" href="/en/coins/filecoin">
          <img class="tw-rounded tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill" loading="lazy" alt="Filecoin" src="https://assets.coingecko.com/coins/images/12817/standard/filecoin.png?1696512609" />
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Filecoin
</div>
</a>
      <div class="tw-flex tw-gap-x-2"></div>
    </div>

</td>
      <td data-view-component="true" class="tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2 tw-whitespace-nowrap"><a target="_blank" rel="nofollow noopener" href="https://www.xt.com/en/trade/fil_usdt?ref=ZHOJUG5" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  FIL/USDT<i data-view-component="true" class="tw-ml-1 fas fa-arrow-up-right-from-square"></i>
</a></div>
</td>
      <td data-sort="4.13889999397408376180571314180088" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="0.0000630207801383767798">$4.14</span>
</td>
      <td data-sort="0.144893" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.14%
</td>
      <td data-sort="181158.20718463272" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $181,158
</td>
      <td data-sort="207088.61911050638" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  $207,089
</td>
      <td data-sort="35.949215008800691313836" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <span data-price-target="price" data-price-btc="35.949215008800691313836">$2,360,970</span>
</td>
      <td data-sort="0.22" data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  0.22%
</td>
      <td data-view-component="true" class="tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <div class="tw-flex tw-gap-x-2"><span class="tw-whitespace-nowrap tw-flex-1">Recently</span></div>
</td>
      <td data-view-component="true" class="tw-text-center tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50">
  <i data-view-component="true" class="fas fa-circle tw-text-success-500 dark:tw-text-success-400"></i>

</td>
</tr>

</tbody>
</table></div>

        <div class="tw-mt-4 gecko-override-links">
          <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-regular">
  Don't see your trading pairs? Click <a target="_blank" href="https://support.coingecko.com/hc/en-us/articles/34239201756569-How-to-add-trading-pairs-on-an-exchange-page">here</a> to learn why.
</div>
        </div>
    </div>

      <div class="tw-flex tw-justify-center tw-w-full tw-mt-4">
        <button data-more-content-target="loadMoreButton" data-action="click-&gt;more-content#loadMoreContent" data-has-price="true" data-url="https://www.coingecko.com/en/exchanges/xt/show_more_tickers?type=spot" type="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      Show more

</div></button>
      </div>
  </div>
</div>


    <div data-view-component="true" class="tw-my-6 lg:tw-my-8 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
    <span data-exchange-show-target="navAnchor" data-key="tab-about"></span>
    <div class="tw-grid tw-grid-cols-1 lg:tw-grid-cols-2 tw-gap-5">
  <!-- About -->
  <div data-view-component="true" class="tw-h-min tw-auto-rows-min tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;*:last-child]:!tw-border-b">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <h2 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  What is XT.COM?
</h2>
      <div data-view-component="true" class="tw-my-1 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  
        XT.COM is a centralized cryptocurrency exchange established in 2018 and is registered in Seychelles. Currently, there are 893 coins and 1016 trading pairs available on the exchange. XT.COM 24h volume is reported to be at $1,072,019,696.09, a change of 8.92331832748232% in the last 24 hours. XT.COM has $47,736,911.89 in Exchange Reserves. The most active trading pair is BTC/USDT with a 24h volume of $340,492,110.40.
          <div class="tw-mt-4">
            By consistently expanding its ecosystem, XT.COM is dedicated to providing users with the most secure, trusted, and hassle-free digital asset trading services. Our exchange is built from a desire to give everyone access to digital assets regardless where you are. 

Founded in 2018, XT.COM now serves more than 6 million registered users, over 500,000+ monthly active users and 40+ million users in the ecosystem. Covering a rich variety of  trading categories together with a NFT aggregated marketplace,  our platform strives to cater to its large user base by providing a secure, trusted and intuitive trading experience.

As the world’s first social-infused digital assets trading platform, XT.COM also supports social networking platform based transactions to make our crypto services more accessible to users all over the world. Furthermore, to ensure optimal data integrity and security, we see user security as our top priority at XT.COM. 
          </div>

</div>
</div>

      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Website
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
            <a href="https://www.xt.com/register?ref=ZHOJUG5" rel="nofollow" role="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      xt.com

</div></a>

</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Community
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
            <div class="tw-flex tw-items-center tw-gap-1 tw-flex-wrap tw-justify-end">
              <a target="_blank" href="https://twitter.com/XTexchange" rel="nofollow noopener" role="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      
                    <span class="tw-flex tw-items-center tw-gap-x-1">
                      <i class="fab fa-x-twitter"></i>
                      Twitter
                    </span>


</div></a>              <a target="_blank" href="https://t.me/XTensupport" rel="nofollow noopener" role="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      
                    <span class="tw-flex tw-items-center tw-gap-x-1">
                      <i class="fab fa-telegram"></i>
                      Telegram
                    </span>


</div></a>          </div>

</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Email
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
            <a href="mailto:support@xt.com" role="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold">
  
      support@xt.com

</div></a>

</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Address
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  -
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Year Established
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  2018
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Recent Monthly Pageviews
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  7,687,079.0
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Alexa Rank
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  #3638
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Incorporation Country Code
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  Seychelles
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Community Data
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  Twitter Followers: 375,404
</div>
</div>

</div>

  <!-- Fees -->
  <div data-view-component="true" class="tw-h-min tw-auto-rows-min tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;*:last-child]:!tw-border-b">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Fees
</h3>

</div>

      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Fees
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  0.2%
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Fiat Deposit
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  CNY
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Withdrawal
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  BTC - 0.001

</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Margin Trading
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  Yes
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Market With Fees
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  Yes
</div>
</div>

</div></div>


    <div data-view-component="true" class="tw-my-6 lg:tw-my-8 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
    <span data-exchange-show-target="navAnchor" data-key="tab-statistics"></span>
    <div class="tw-grid tw-grid-cols-2 tw-gap-4">
  <div data-view-component="true" class="tw-col-span-2 lg:tw-col-span-1 !tw-divide-none tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Volume by Market Pair
</h3>

</div>

    

    <div id="exchange-pair-volume-chart-d14609b3"
         data-controller="pie-chart"
         data-data-json="[{&quot;name&quot;:&quot;BTC/USDT&quot;,&quot;y&quot;:31.78},{&quot;name&quot;:&quot;ETH/USDT&quot;,&quot;y&quot;:11.74},{&quot;name&quot;:&quot;NEIRO/USDT&quot;,&quot;y&quot;:5.37},{&quot;name&quot;:&quot;XT/USDT&quot;,&quot;y&quot;:1.77},{&quot;name&quot;:&quot;ETH/USDC&quot;,&quot;y&quot;:1.39},{&quot;name&quot;:&quot;DOGE/USDT&quot;,&quot;y&quot;:1.17},{&quot;name&quot;:&quot;SEI/USDT&quot;,&quot;y&quot;:1.09},{&quot;name&quot;:&quot;SOL/USDT&quot;,&quot;y&quot;:0.99},{&quot;name&quot;:&quot;HMSTR/USDT&quot;,&quot;y&quot;:0.95},{&quot;name&quot;:&quot;BNB/USDT&quot;,&quot;y&quot;:0.89},{&quot;name&quot;:&quot;CAT/USDT&quot;,&quot;y&quot;:0.87},{&quot;name&quot;:&quot;AAVE/USDT&quot;,&quot;y&quot;:0.65},{&quot;name&quot;:&quot;INJ/USDT&quot;,&quot;y&quot;:0.65},{&quot;name&quot;:&quot;WIF/USDT&quot;,&quot;y&quot;:0.62},{&quot;name&quot;:&quot;PEOPLE/USDT&quot;,&quot;y&quot;:0.62},{&quot;name&quot;:&quot;STRK/USDT&quot;,&quot;y&quot;:0.61},{&quot;name&quot;:&quot;STX/USDT&quot;,&quot;y&quot;:0.61},{&quot;name&quot;:&quot;TAO/USDT&quot;,&quot;y&quot;:0.59},{&quot;name&quot;:&quot;XRP/USDT&quot;,&quot;y&quot;:0.56},{&quot;name&quot;:&quot;MOODENG/USDT&quot;,&quot;y&quot;:0.56},{&quot;name&quot;:&quot;FTM/USDT&quot;,&quot;y&quot;:0.56},{&quot;name&quot;:&quot;NEAR/USDT&quot;,&quot;y&quot;:0.49},{&quot;name&quot;:&quot;WLD/USDT&quot;,&quot;y&quot;:0.44},{&quot;name&quot;:&quot;ARB/USDT&quot;,&quot;y&quot;:0.43},{&quot;name&quot;:&quot;FIDA/USDT&quot;,&quot;y&quot;:0.42},{&quot;name&quot;:&quot;SAGA/USDT&quot;,&quot;y&quot;:0.38},{&quot;name&quot;:&quot;CHZ/USDT&quot;,&quot;y&quot;:0.36},{&quot;name&quot;:&quot;TRX/USDT&quot;,&quot;y&quot;:0.36},{&quot;name&quot;:&quot;LINK/USDT&quot;,&quot;y&quot;:0.35},{&quot;name&quot;:&quot;MOTHER/USDT&quot;,&quot;y&quot;:0.34},{&quot;name&quot;:&quot;AVAX/USDT&quot;,&quot;y&quot;:0.33},{&quot;name&quot;:&quot;PHB/USDT&quot;,&quot;y&quot;:0.33},{&quot;name&quot;:&quot;ETH/XTUSD&quot;,&quot;y&quot;:0.32},{&quot;name&quot;:&quot;EDLC/USDT&quot;,&quot;y&quot;:0.31},{&quot;name&quot;:&quot;FET/USDT&quot;,&quot;y&quot;:0.31},{&quot;name&quot;:&quot;USDC/USDT&quot;,&quot;y&quot;:0.3},{&quot;name&quot;:&quot;LTC/USDT&quot;,&quot;y&quot;:0.3},{&quot;name&quot;:&quot;ADA/USDT&quot;,&quot;y&quot;:0.29},{&quot;name&quot;:&quot;FLOKI/USDT&quot;,&quot;y&quot;:0.29},{&quot;name&quot;:&quot;MOG/USDT&quot;,&quot;y&quot;:0.29},{&quot;name&quot;:&quot;AR/USDT&quot;,&quot;y&quot;:0.29},{&quot;name&quot;:&quot;XMR/USDT&quot;,&quot;y&quot;:0.28},{&quot;name&quot;:&quot;CELO/USDT&quot;,&quot;y&quot;:0.28},{&quot;name&quot;:&quot;NOT/USDT&quot;,&quot;y&quot;:0.27},{&quot;name&quot;:&quot;BONK/USDT&quot;,&quot;y&quot;:0.26},{&quot;name&quot;:&quot;CORE/USDT&quot;,&quot;y&quot;:0.26},{&quot;name&quot;:&quot;NEIROETH/USDT&quot;,&quot;y&quot;:0.25},{&quot;name&quot;:&quot;POPCAT/USDT&quot;,&quot;y&quot;:0.23},{&quot;name&quot;:&quot;UNI/USDT&quot;,&quot;y&quot;:0.23},{&quot;name&quot;:&quot;FIL/USDT&quot;,&quot;y&quot;:0.22},{&quot;name&quot;:&quot;EOS/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;CRV/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;SATS/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;DYDX/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;ATOM/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;BOME/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;SUPER/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;PENDLE/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;RATS/USDT&quot;,&quot;y&quot;:0.21},{&quot;name&quot;:&quot;BABYBONK/USDT&quot;,&quot;y&quot;:0.2},{&quot;name&quot;:&quot;BCH/USDT&quot;,&quot;y&quot;:0.2},{&quot;name&quot;:&quot;ARKM/USDT&quot;,&quot;y&quot;:0.2},{&quot;name&quot;:&quot;ORDI/USDT&quot;,&quot;y&quot;:0.19},{&quot;name&quot;:&quot;AXL/USDT&quot;,&quot;y&quot;:0.19},{&quot;name&quot;:&quot;BRETT/USDT&quot;,&quot;y&quot;:0.19},{&quot;name&quot;:&quot;SLF/USDT&quot;,&quot;y&quot;:0.19},{&quot;name&quot;:&quot;GMT/USDT&quot;,&quot;y&quot;:0.19},{&quot;name&quot;:&quot;MEW/USDT&quot;,&quot;y&quot;:0.19},{&quot;name&quot;:&quot;KAVA/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;ARPA/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;OM/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;HOOK/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;APT/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;BTC/USDC&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;BLUR/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;SHRAP/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;AUCTION/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;TON/USDT&quot;,&quot;y&quot;:0.18},{&quot;name&quot;:&quot;ICE/USDT&quot;,&quot;y&quot;:0.17},{&quot;name&quot;:&quot;LOKA/USDT&quot;,&quot;y&quot;:0.17},{&quot;name&quot;:&quot;ENA/USDT&quot;,&quot;y&quot;:0.17},{&quot;name&quot;:&quot;GALA/USDT&quot;,&quot;y&quot;:0.17},{&quot;name&quot;:&quot;SMH/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;DOGS/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;ETHFI/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;MINA/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;MANTA/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;COTI/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;IMX/USDT&quot;,&quot;y&quot;:0.16},{&quot;name&quot;:&quot;LUNA/USDT&quot;,&quot;y&quot;:0.15},{&quot;name&quot;:&quot;XZERO/USDT&quot;,&quot;y&quot;:0.15},{&quot;name&quot;:&quot;XLM/USDT&quot;,&quot;y&quot;:0.15},{&quot;name&quot;:&quot;ROSE/USDT&quot;,&quot;y&quot;:0.15},{&quot;name&quot;:&quot;BILLY/USDT&quot;,&quot;y&quot;:0.15},{&quot;name&quot;:&quot;VET/USDT&quot;,&quot;y&quot;:0.15},{&quot;name&quot;:&quot;CKB/USDT&quot;,&quot;y&quot;:0.14},{&quot;name&quot;:&quot;AGI/USDT&quot;,&quot;y&quot;:0.14},{&quot;name&quot;:&quot;VGX/USDT&quot;,&quot;y&quot;:0.14},{&quot;name&quot;:&quot;SNX/USDT&quot;,&quot;y&quot;:0.14},{&quot;name&quot;:&quot;CTK/USDT&quot;,&quot;y&quot;:0.14},{&quot;name&quot;:&quot;MKR/USDT&quot;,&quot;y&quot;:0.13}]"
         data-is-percentage="true"
         class="!tw-h-[450px] md:!tw-h-[250px]">
      <div class="tw-flex tw-w-full tw-h-full tw-items-center tw-justify-center">
          <span class="tw-h-fit dark:tw-text-moon-50">
            <i class="far fa-fw fa-spinner-third fa-spin tw-text-2xl"></i>
          </span>
      </div>
    </div>


</div>
  <div data-view-component="true" class="tw-col-span-2 lg:tw-col-span-1 !tw-divide-none tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Volume by Currency
</h3>

</div>

    

    <div id="exchange-currency-volume-chart-9c42fe8e"
         data-controller="pie-chart"
         data-data-json="[{&quot;name&quot;:&quot;USDT&quot;,&quot;y&quot;:80.32000000000001},{&quot;name&quot;:&quot;USDC&quot;,&quot;y&quot;:1.5699999999999998},{&quot;name&quot;:&quot;XTUSD&quot;,&quot;y&quot;:0.32}]"
         data-is-percentage="true"
         class="!tw-h-[450px] md:!tw-h-[250px]">
      <div class="tw-flex tw-w-full tw-h-full tw-items-center tw-justify-center">
          <span class="tw-h-fit dark:tw-text-moon-50">
            <i class="far fa-fw fa-spinner-third fa-spin tw-text-2xl"></i>
          </span>
      </div>
    </div>


</div>

  <div data-view-component="true" class="tw-h-min tw-auto-rows-min !tw-divide-none tw-col-span-2 chart-group tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <div class="tw-flex tw-flex-col lg:tw-flex-row tw-gap-2 tw-justify-between">
        <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Exchange Trade Volume
</h3>
        <div x-data="{ activeButton: &#39;&#39; }" x-init="activeButton = &#39;range-24h&#39;" data-coin-chart-target="rangeSelector" role="group" data-view-component="true" class="!tw-h-fit tw-p-1 tw-bg-gray-100 dark:tw-bg-moon-800 tw-rounded-lg tw-w-fit tw-isolate">
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:volumes" data-url="/exchanges/404/usd/24_hours.json" id="range-24h" @click="activeButton = &#39;range-24h&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-24h&#39; }" type="button" data-view-component="true" class="gecko-button-group-item selected">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    24h

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:volumes" data-url="/exchanges/404/usd/7_days.json" id="range-7d" @click="activeButton = &#39;range-7d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-7d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    7d

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:volumes" data-url="/exchanges/404/usd/14_days.json" id="range-14d" @click="activeButton = &#39;range-14d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-14d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    14d

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:volumes" data-url="/exchanges/404/usd/30_days.json" id="range-30d" @click="activeButton = &#39;range-30d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-30d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    1m

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:volumes" data-url="/exchanges/404/usd/3_months.json" id="range-90d" @click="activeButton = &#39;range-90d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-90d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    3m

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:volumes" data-url="/exchanges/404/usd/1_year.json" id="range-1y" @click="activeButton = &#39;range-1y&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-1y&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    1y

</span></button>
    <button data-action="click-&gt;exchange-show#showExportDropdown exchange-show:click:outside-&gt;exchange-show#hideExportDropdown" data-exchange-show-target="exportButton" data-login-state-target="exportDataButton" id="export" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    <i data-view-component="true" class="far fa-fw fa-arrow-down-to-bracket"></i>


</span></button>
</div>
        <!-- Export Dropdown -->
        <div data-exchange-show-target="exportDropdownMenu" data-login-state-target="exportDataDropdown" data-view-component="true" class="tw-hidden tw-z-10">
  <div class="tw-z-[2000]">
  <div x-transition:enter="tw-transition tw-ease-out tw-duration-100" x-transition:enter-end="tw-transform tw-opacity-100 tw-scale-100" x-transition:enter-start="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave="tw-transition tw-ease-in tw-duration-75" x-transition:leave-end="tw-transform tw-opacity-0 tw-scale-95" x-transition:leave-start="tw-transform tw-opacity-100 tw-scale-100" data-view-component="true" class="dark:tw-bg-moon-800 dark:tw-ring-moon-700 focus:tw-outline-none tw-bg-white tw-mt-2 tw-origin-top-left tw-ring-2 tw-ring-gray-200 tw-rounded-md tw-shadow-lg tw-w-56 tw-p-2 tw-z-[2000]">
    
      <div data-view-component="true">
  
              <span data-url="/exchanges/xt/export.csv" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  CSV
  
</span>
            <span data-url="/exchanges/xt/export.xls" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  Excel
  
</span>

</div>

</div></div></div>      </div>

</div>

    

    <div id="exchange-volume-chart-be0e4dee"
         data-controller="generic-chart"
         data-label="Trade Volume"
         data-data-url="/exchanges/404/usd/24_hours.json"
         data-chart-type="exchange:volumes"
         class="!tw-h-[500px]">
      <div class="tw-flex tw-w-full tw-h-full tw-items-center tw-justify-center">
          <span class="tw-h-fit dark:tw-text-moon-50">
            <i class="far fa-fw fa-spinner-third fa-spin tw-text-2xl"></i>
          </span>
      </div>
    </div>


</div>
    <div data-view-component="true" class="tw-h-min tw-auto-rows-min !tw-divide-none tw-col-span-2 chart-group tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
          <div class="tw-flex tw-flex-col lg:tw-flex-row tw-gap-2 tw-justify-between">
          <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Exchange Normalized Trade Volume
</h3>
          <div x-data="{ activeButton: &#39;&#39; }" x-init="activeButton = &#39;range-24h&#39;" data-coin-chart-target="rangeSelector" role="group" data-view-component="true" class="!tw-h-fit tw-p-1 tw-bg-gray-100 dark:tw-bg-moon-800 tw-rounded-lg tw-w-fit tw-isolate">
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:normalizedVolumes" data-url="/exchanges/404/usd/24_hours.json" id="range-24h" @click="activeButton = &#39;range-24h&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-24h&#39; }" type="button" data-view-component="true" class="gecko-button-group-item selected">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    24h

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:normalizedVolumes" data-url="/exchanges/404/usd/7_days.json" id="range-7d" @click="activeButton = &#39;range-7d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-7d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    7d

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:normalizedVolumes" data-url="/exchanges/404/usd/14_days.json" id="range-14d" @click="activeButton = &#39;range-14d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-14d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    14d

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:normalizedVolumes" data-url="/exchanges/404/usd/30_days.json" id="range-30d" @click="activeButton = &#39;range-30d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-30d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    1m

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:normalizedVolumes" data-url="/exchanges/404/usd/3_months.json" id="range-90d" @click="activeButton = &#39;range-90d&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-90d&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    3m

</span></button>
    <button data-action="click-&gt;exchange-show#handleChartChange" data-chart="exchange:normalizedVolumes" data-url="/exchanges/404/usd/1_year.json" id="range-1y" @click="activeButton = &#39;range-1y&#39;; " :class="{ &#39;selected&#39;: activeButton === &#39;range-1y&#39; }" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    1y

</span></button>
    <button data-action="click-&gt;exchange-show#toggleCalendar" data-exchange-show-target="calendarButton" id="calendar" type="button" data-view-component="true" class="gecko-button-group-item">
  <span data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
    <i data-view-component="true" class="far fa-fw fa-calendar-week"></i>


</span></button>
</div>        </div>

</div>

    

      <div id="exchange-normalized-volume-chart-637a018b"
           data-controller="generic-chart"
           data-label="Trade Volume"
           data-data-url="/exchanges/404/usd/24_hours.json"
           data-chart-type="exchange:normalizedVolumes"
           class="!tw-h-[500px]">
        <div class="tw-flex tw-w-full tw-h-full tw-items-center tw-justify-center">
            <span class="tw-h-fit dark:tw-text-moon-50">
              <i class="far fa-fw fa-spinner-third fa-spin tw-text-2xl"></i>
            </span>
        </div>
      </div>


</div></div>


    <div data-view-component="true" class="tw-my-6 lg:tw-my-8 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
      <span data-exchange-show-target="navAnchor" data-key="tab-trust-score"></span>
      <div class="tw-grid tw-grid-cols-1 2lg:tw-grid-cols-3 tw-gap-4">
        <div class="tw-col-span-1">
              <div data-view-component="true" class="tw-h-min tw-auto-rows-min tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
          <div class="tw-flex tw-items-center tw-gap-x-1 tw-mb-5">
          <h2 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  XT.COM Trust Score
</h2>
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Trust Score is a rating algorithm developed by CoinGecko to evaluate the legitimacy of an exchange’s trading volume. Trust Score is calculated on a range of metrics such as liquidity, scale of operations, cybersecurity score, and more. For more details read our <a href="https://www.coingecko.com/en/methodology" target="_blank">full methodology</a>.
      <div data-popper-arrow></div>
    </div>
  </div>
</span>        </div>

        <div data-view-component="true" class="tw-mb-1 tw-font-bold tw-text-success-500 dark:tw-text-success-400 tw-text-4xl md:tw-text-5xl">
  8/10
</div>

</div>

      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            Liquidity
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Liquidity refers to how likely a cryptoasset can be traded at a price which reflects its intrinsic value. To measure liquidity, we consider an exchange's:
<br>(1) Web traffic &amp; Reported Volume
<br>(2) Order book spread
<br>(3) Trading Activity
<br>(4) Trust Score on Trading Pairs

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  2.0
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            Scale
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Scale of Operations refers to parameters that can be measured directly through an exchange's reported numbers, yet don't necessarily correlate with liquidity. To measure Scale of Operations, we considers an exchange's:
<br>(1) Normalized Trading Volume Percentile
<br>(2) Normalized Order Book Depth Percentile

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  1.0
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            Cybersecurity
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Cybersecurity Score of a cryptocurrency exchange as evaluated by Hacken on cer.live.
<br>This evaluation covers product, infrastructure, user accounts as well as several other security aspects of an exchange.

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  1.5
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            API Coverage
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      API Coverage measures the completeness of an exchanges API for the following criterias:
<br>(1) Tickers Data
<br>(2) Historical Trades Data
<br>(3) Order Book Data
<br>(4) Candlestick/OHLC
<br>(5) WebSocket API
<br>(6) API Trading
<br>(7) Public Documentation

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  0.5
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            Team
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Team refers to the public profile availability of Senior Leadership team.
<br>Score 0.5 = Public profiles of senior team members are known and available as reference on reputable sites.
<br>Score 0 = Little to no public presence of senior leadership team, or has no public profiles.

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  0.5
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            Incident
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Incident refers to whether an exchange has experienced security/functional issues that can potentially affect a user's fund safety.
<br>Score 1.0 = exchange has no incident recorded
<br>Score 0.5 = exchange has minor incident(s) recorded
<br>Score 0 = exchange has major incident(s) recorded

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  1.0
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            PoR
          <span data-controller="tooltip" data-tooltip-tooltip-placement-value="bottom" data-action="mouseleave-&gt;tooltip#hide">
  <div data-tooltip-target="anchor" data-action="mouseenter->tooltip#show" aria-describedby="tooltip" class="tw-inline-block">
    <i data-view-component="true" class="far fa-info-circle fa-fw"></i>

  </div>
  <div>
    <div role="tooltip" class="gecko-override-links gecko-tooltip !tw-hidden gecko-tooltip-long gecko-tooltip-extra-padding" data-tooltip-target="tooltip">
      Proof of Reserves (PoR) considers the availability of declared assets that can be publicly assessed, user-attestation processes as well as financial audits. Read more about it <a href="https://www.coingecko.com/learn/what-is-proof-of-reserves-por">here</a>.

      <div data-popper-arrow></div>
    </div>
  </div>
</span>
</div>
    <div data-view-component="true" class="tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  1.0
</div>
</div>

</div>
        </div>
        <div class="tw-col-span-1 2lg:tw-col-span-2 tw-flex tw-flex-col tw-gap-4 2lg:tw-col-start-2">
          <div data-view-component="true" class="tw-h-fit tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
      <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Liquidity
</h3>

</div>

      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Reported Trading Volume
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span data-price-target="price" data-price-btc="16314.0840492194075511">-</span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Normalized Trading Volume
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span data-price-target="price" data-price-btc="16262.4870683357487742">-</span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Reported-Normalized Volume Ratio
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  0.997
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Average Bid-Ask Spread
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  1.87%
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Trading Pair Total Trust Score
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
        <div data-view-component="true" class="tw-w-full tw-w-[150px] tw-bg-gray-200 tw-rounded-full tw-h-1.5 tw-my-2 tw-flex dark:tw-bg-moon-700">
      <span class="tw-bg-success-500 dark:tw-bg-success-400 first:tw-rounded-l last:tw-rounded-r" style="width: 77.58%" data-tooltip="623"></span>
      <span class="tw-bg-warning-500 first:tw-rounded-l last:tw-rounded-r" style="width: 21.05%" data-tooltip="169"></span>
      <span class="tw-bg-danger-500 first:tw-rounded-l last:tw-rounded-r" style="width: 1.37%" data-tooltip="11"></span>
</div>
</div>
</div>

</div>

<div data-view-component="true" class="tw-h-fit tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;*:last-child]:!tw-border-b">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
      <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Scale
</h3>

</div>

      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Normalized Volume Percentile
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  98th
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Combined Orderbook Percentile
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  96th
</div>
</div>

</div>

    <div data-view-component="true" class="tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;*:last-child]:!tw-border-b">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
          <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Cybersecurity
</h3>
        <div class="tw-mb-1 tw-mt-5"><img width="240px" loading="lazy" class="tw-block dark:tw-hidden" src="https://static.coingecko.com/s/cer_live_2stars-3bec34533ab2d924922861d8c665897189bae3178bf8abf79a1288dafe8b23bb.svg" /><img width="240px" loading="lazy" class="tw-hidden dark:tw-block" src="https://static.coingecko.com/s/cer_live_2stars-dark-mode-d35bbe97ffb907c35ecf83cbf023f6569077a23f64fc574f668cb03b109e07df.svg" /></div>

</div>

      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Penetration Test
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Proof of Reserves Audit
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-danger-500 fa-times"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Bug Bounty
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto gecko-override-links tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Last Updated: 2024-09-25 | Data provided by <a href="https://bit.ly/31r8HL9" rel="nofollow">cer.live</a>
</div>
    
</div>

</div>

  <div data-view-component="true" class="tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;*:last-child]:!tw-border-b">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  API Coverage
</h3>

</div>

      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Grade
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  A
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Tickers Data
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Historical Trades Data
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Orderbook Data
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Trading via API
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  OHLC Data
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Websocket
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Public Documentation
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
          <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
        <a target="_blank" rel="noopener nofollow" href="https://www.xt.com/help/restApi" data-view-component="true" class="tw-ml-0.5 !tw-text-success-500 dark:!tw-text-success-400 tw-cursor-pointer tw-font-regular tw-text-gray-700 hover:tw-text-primary-500 dark:tw-text-moon-200 dark:hover:tw-text-primary-400">  [source]</a>

</div>
</div>
      <div data-view-component="true" class="tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto gecko-override-links tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
            Last Updated: 2019-09-11

</div>
    
</div>

</div>

  <div data-view-component="true" class="tw-p-4 tw-rounded-xl tw-ring-2 tw-ring-gray-200 dark:tw-ring-moon-700 tw-grid tw-grid-cols-1 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&amp;&gt;*:last-child]:!tw-border-b">
  <div data-view-component="true" class="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
        <h3 data-view-component="true" class="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Team
</h3>

</div>

      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Team is public
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
</div>
</div>
      <div data-view-component="true" class="!tw-grid tw-grid-cols-2 tw-flex tw-justify-between tw-py-3">
    <div data-view-component="true" class="tw-my-auto tw-text-left tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-text-sm tw-leading-5">
  Team profile page
</div>
    <div data-view-component="true" class="tw-my-auto !tw-text-left tw-pl-2 tw-text-right tw-text-gray-900 dark:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
          <span><i class="far tw-text-success-500 dark:tw-text-success-400 fa-check"></i></span>
        <a target="_blank" rel="noopener nofollow" href="https://www.linkedin.com/company/xt-com-exchange/people/" data-view-component="true" class="tw-ml-0.5 !tw-text-success-500 dark:!tw-text-success-400 tw-cursor-pointer tw-font-regular tw-text-gray-700 hover:tw-text-primary-500 dark:tw-text-moon-200 dark:hover:tw-text-primary-400">  [source]</a>

</div>
</div>

</div>


        </div>
      </div>
  </div>
</div>

  </main>

    <div
    class="tw-justify-center tw-items-center tw-w-fit tw-mx-auto"
    data-ads-target="banner"
  >
    <!-- /8691100/CoinGecko_S2S_Footer_ROS -->
    <div data-aaad="true" data-aa-adunit="/22743369056/CoinGecko_S2S_Footer_ROS"></div>
  </div>

</div>
<!-- END: Page Content -->


<!-- START: Footer Content -->
  <footer class="tw-mt-8">
      <div data-controller="footer">
  <!-- Footer Links -->
  <div data-view-component="true" class="tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
  <div class="container tw-block lg:tw-flex tw-items-center tw-my-6" id="footer-links">
    <div class="lg:tw-grid lg:tw-grid-cols-7 lg:tw-gap-x-8" data-controller="footer">
      <div class="lg:tw-col-span-3">
        <a class="tw-inline-block tw-h-12" href="/">
          <img alt="CoinGecko" class="!tw-h-full tw-block dark:tw-hidden" src="https://static.coingecko.com/s/coingecko-logo-8903d34ce19ca4be1c81f0db30e924154750d208683fad7ae6f2ce06c76d0a56.png" />
          <img alt="CoinGecko" class="!tw-h-full tw-hidden dark:tw-block" src="https://static.coingecko.com/s/coingecko-logo-white-ea42ded10e4d106e14227d48ea6140dc32214230aa82ef63d0499f9c1e109656.png" />
</a>        <div data-view-component="true" class="tw-mt-5 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CoinGecko provides a fundamental analysis of the crypto market. In addition to tracking price, volume and market capitalisation, CoinGecko tracks community growth, open-source code development, major events and on-chain metrics.
</div>
      </div>

      <!-- Resources / Donations -->
      <div class="tw-mt-8 lg:tw-mt-0">
        <!-- Resources -->
        <div class="tw-flex tw-flex-col lg:tw-space-y-4">
          <div class="tw-py-4 lg:tw-py-0 tw-flex lg:tw-block tw-items-center tw-cursor-pointer lg:tw-cursor-auto tw-border-0 tw-border-b tw-border-t lg:tw-border-b-0 lg:tw-border-t-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" data-action="click->footer#toggleFooterGroup" id="footer-links-resources">
            <div data-view-component="true" class="tw-flex-1 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Resources
</div>
            <span class="lg:tw-hidden">
              <i class="far fa-fw fa-plus tw-text-lg dark:tw-text-moon-50"></i>
            </span>
          </div>
          <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mt-0 lg:tw-mt-2 tw-h-0 lg:tw-h-auto tw-overflow-y-hidden tw-pl-2 lg:tw-pl-0 lg:tw-pb-0 tw-border-0 lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" id="footer-links-resources-group">
            <a href="/en/news">
              <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Crypto News
</div>
</a>
            <a href="/en/public-companies-bitcoin">
              <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Bitcoin Treasury
</div>
</a>
            <a href="/en/cryptocurrency-heatmap">
              <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Crypto Heatmap
</div>
</a>
            <a href="/en/api">
              <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Crypto API
</div>
</a>          </div>
        </div>

        <!-- Donations -->
        <div class="tw-flex tw-flex-col lg:tw-space-y-4 lg:tw-mt-6">
          <div class="tw-py-4 lg:tw-pb-0 tw-flex lg:tw-block tw-items-center tw-cursor-pointer lg:tw-cursor-auto tw-border-0 tw-border-b lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" data-action="click->footer#toggleFooterGroup" id="footer-links-donations">
            <div data-view-component="true" class="tw-flex-1 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Donations
</div>
            <span class="lg:tw-hidden">
              <i class="far fa-fw fa-plus tw-text-lg dark:tw-text-moon-50"></i>
            </span>
          </div>
          <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mt-0 lg:tw-mt-2 tw-h-0 lg:tw-h-auto tw-overflow-y-hidden tw-pl-2 lg:tw-pl-0 lg:tw-pb-0 tw-border-0 lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" id="footer-links-donations-group">
              <div onclick="Modal.show(&#39;donate_btc_modal&#39;)" data-view-component="true" class="tw-cursor-pointer tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Bitcoin
</div>
              <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="donate_btc_modal" x-cloak="true" x-data="modalToggleable(&#39;donate_btc_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-center">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="donate_btc_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="donate_btc_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        <div data-view-component="true" class="tw-pt-3 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Donate Bitcoin
</div>
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
                    <img loading="lazy" class="tw-block tw-mx-auto tw-mb-8" width="175" height="175" src="https://static.coingecko.com/s/donations_qrcode/bitcoin_address-0c641f25960938f692e238c986cf0719ea871e94617dd28202823ae8ffa14a74.png" />

                  <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input label="Donation Address" value="3KJmVaMzKRxKbKTMQmfnKzecpsExs8tbkk" type="text" data-view-component="true" class="gecko-input"></input>

    <div data-view-component="true" class="tw-flex tw-items-center tw-px-1 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
                        <button data-action="click-&gt;footer#copyDonationAddress" type="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-inline-flex">

    <div data-view-component="true" class="tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      
                        <i data-view-component="true" class="far fa-fw fa-copy"></i>



</div></button>
</div>
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
</div>
      
</div></div></div>              <div onclick="Modal.show(&#39;donate_eth_modal&#39;)" data-view-component="true" class="tw-cursor-pointer tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Ethereum
</div>
              <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="donate_eth_modal" x-cloak="true" x-data="modalToggleable(&#39;donate_eth_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-center">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="donate_eth_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="donate_eth_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        <div data-view-component="true" class="tw-pt-3 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Donate Ethereum
</div>
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
                    <img loading="lazy" class="tw-block tw-mx-auto tw-mb-8" width="175" height="175" src="https://static.coingecko.com/s/donations_qrcode/ethereum_address-5e5ffeae71cb953fc5b12ebdf4205060a60bd35338de0465cad78ddf78db5c9d.png" />

                  <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input label="Donation Address" value="0x4Cdc86fa95Ec2704f0849825f1F8b077deeD8d39" type="text" data-view-component="true" class="gecko-input"></input>

    <div data-view-component="true" class="tw-flex tw-items-center tw-px-1 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
                        <button data-action="click-&gt;footer#copyDonationAddress" type="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-inline-flex">

    <div data-view-component="true" class="tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      
                        <i data-view-component="true" class="far fa-fw fa-copy"></i>



</div></button>
</div>
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
</div>
      
</div></div></div>          </div>
        </div>
      </div>

      <!-- Support -->
      <div class="tw-flex tw-flex-col lg:tw-space-y-4">
        <div class="tw-py-4 lg:tw-py-0 tw-flex lg:tw-block tw-items-center tw-cursor-pointer lg:tw-cursor-auto tw-border-0 tw-border-b lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" data-action="click->footer#toggleFooterGroup" id="footer-links-support">
          <div data-view-component="true" class="tw-flex-1 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Support
</div>
          <span class="lg:tw-hidden">
          <i class="far fa-fw fa-plus tw-text-lg dark:tw-text-moon-50"></i>
        </span>
        </div>
        <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mt-0 lg:tw-mt-2 tw-h-0 lg:tw-h-auto tw-overflow-y-hidden tw-pl-2 lg:tw-pl-0 lg:tw-pb-0 tw-border-0 lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" id="footer-links-support-group">
          <a href="/request-form?locale=en">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Request Form
</div>
</a>
          <a href="https://gcko.io/coingeckoads">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Advertising
</div>
</a>
          <a href="/en/candy/partners-getting-started">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Candy Rewards Listing
</div>
</a>
          <a href="https://support.coingecko.com/">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Help Center
</div>
</a>
          <a href="https://hackenproof.com/coingecko/coingecko">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Bug Bounty
</div>
</a>
          <a href="/en/faq">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  FAQ
</div>
</a>        </div>
      </div>

      <!-- About CoinGecko -->
      <div class="tw-flex tw-flex-col lg:tw-space-y-4">
        <div class="tw-py-4 lg:tw-py-0 tw-flex lg:tw-block tw-items-center tw-cursor-pointer lg:tw-cursor-auto tw-border-0 tw-border-b lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" data-action="click->footer#toggleFooterGroup" id="footer-links-about-coingecko">
          <div data-view-component="true" class="tw-flex-1 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  About CoinGecko
</div>
          <span class="lg:tw-hidden">
            <i class="far fa-fw fa-plus tw-text-lg dark:tw-text-moon-50"></i>
          </span>
        </div>
        <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mt-0 lg:tw-mt-2 tw-h-0 lg:tw-h-auto tw-overflow-y-hidden tw-pl-2 lg:tw-pl-0 lg:tw-pb-0 tw-border-0 lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" id="footer-links-about-coingecko-group">
          <a href="/en/about">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  About Us
</div>
</a>
          <a target="_blank" href="https://careers.coingecko.com/">
            <div data-view-component="true" class="tw-inline-block tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Careers
</div>
            <!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<span data-view-component="true" class="tw-inline-flex tw-items-center tw-px-1.5 tw-py-0.5 tw-bg-primary-100 dark:tw-bg-primary-400/10 tw-rounded-md">
    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-primary-700 dark:tw-text-primary-400 tw-font-medium">
  
      Join Us

</div></span><!-- TODO: remove dropdown conditionals along dropdown deprecation -->
<!-- TODO: remove dropdown conditionals along dropdown deprecation -->

</a>
          <a target="_blank" rel="noopener" href="https://blog.coingecko.com/">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Company Blog
</div>
</a>
          <a href="https://brand.coingecko.com">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Branding Guide
</div>
</a>
          <a href="/en/methodology">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Methodology
</div>
</a>
          <a href="/en/disclaimer">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Disclaimer
</div>
</a>
          <a href="/en/terms">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Terms of Service
</div>
</a>
          <a href="/en/privacy">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Privacy Policy
</div>
</a>
          <a href="/en/ad-policy">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Ad Policy
</div>
</a>
          <div id="ot-sdk-btn" class="tw-text-sm tw-text-gray-500 tw-font-normal tw-leading-5 tw-cursor-pointer dark:tw-text-moon-200">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Cookie Preferences
</div>
          </div>
        </div>
      </div>

      <!-- Community -->
      <div class="tw-flex tw-flex-col lg:tw-space-y-4">
        <div class="tw-py-4 lg:tw-py-0 tw-flex lg:tw-block tw-items-center tw-cursor-pointer lg:tw-cursor-auto tw-border-0 tw-border-b lg:tw-border-b-0 lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" data-action="click->footer#toggleFooterGroup" id="footer-links-community">
          <div data-view-component="true" class="tw-flex-1 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Community
</div>
          <span class="lg:tw-hidden">
            <i class="far fa-fw fa-plus tw-text-lg dark:tw-text-moon-50"></i>
          </span>
        </div>
        <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mt-0 lg:tw-mt-2 tw-h-0 lg:tw-h-auto tw-overflow-y-hidden tw-pl-2 lg:tw-pl-0 lg:tw-pb-0 tw-border-0 lg:tw-border-b-0 tw-border-solid tw-border-gray-200 dark:tw-border-white dark:tw-border-opacity-12" id="footer-links-community-group">
          <a target="_blank" rel="noopener" href="https://twitter.com/coingecko">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  X/Twitter
</div>
</a>
          <a target="_blank" rel="noopener" href="https://t.me/coingecko">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Telegram Chat
</div>
</a>
          <a target="_blank" rel="noopener" href="https://t.me/coingeckonews">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Telegram News
</div>
</a>
          <a target="_blank" rel="noopener" href="https://www.instagram.com/coingecko/">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Instagram
</div>
</a>
          <a target="_blank" rel="noopener" href="https://www.reddit.com/r/coingecko/">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Reddit
</div>
</a>
          <a target="_blank" rel="noopener" href="https://discord.gg/EhrkaCH">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Discord
</div>
</a>
          <a target="_blank" rel="noopener" href="https://www.facebook.com/coingecko">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Facebook
</div>
</a>
          <a target="_blank" rel="noopener" href="https://www.youtube.com/channel/UC-OTgwOAI7KmP0eDAtqN3Ow?sub_confirmation=1">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Youtube
</div>
</a>
          <a target="_blank" rel="noopener" href="https://www.tiktok.com/@coingeckotv">
            <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  TikTok
</div>
</a>        </div>
      </div>
    </div>
  </div>


  <!-- Newsletter CTA -->
  <div data-view-component="true" class="tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
  <div class="container tw-block lg:tw-flex tw-items-center tw-my-6" id="footer-newsletter" data-controller="newsletter">
    <div class="tw-block lg:tw-flex-1">
      <div data-view-component="true" class="tw-mb-2 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Interested to stay up-to-date with cryptocurrencies?
</div>
      <div data-view-component="true" class="tw-mb-2 lg:tw-mb-0 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Get the latest crypto news, updates, and reports by subscribing to our free newsletter.
</div>
    </div>
    <div>
      <form class="tw-block lg:tw-flex tailwind-reset tw-justify-end tw-mb-1">
        <div class="tw-mb-2 lg:tw-mb-0 lg:tw-mr-2">
          <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input data-newsletter-target="emailInput" placeholder="Enter your email address" type="email" data-view-component="true" class="!tw-h-10 gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
        </div>
        <div>
          <button data-action="newsletter#subscribeNewsletter" data-campaign-id="w" type="button" data-view-component="true" class="tw-w-full lg:tw-w-auto tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-inline-flex">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Subscribe

</div></button>
        </div>
      </form>
    </div>
  </div>


  <!-- Copyright / App Store Links -->
  <div data-view-component="true" class="tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
  <div class="container tw-block lg:tw-flex tw-items-center tw-my-6 tw-text-center lg:tw-text-left" id="footer-copyright">
    <div class="tw-block lg:tw-flex-1 tw-mb-4 lg:tw-mb-0">
      <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  © 2024 CoinGecko. All Rights Reserved.
</div>
    </div>

    <div class="tw-block lg:tw-flex">
      <a target="_blank" rel="noopener" href="https://coingecko.app.link/footer-android">
        <img loading="lazy" alt="Google Play Store Button" width="135" height="40" class="tw-mr-2" src="https://static.coingecko.com/s/coingecko_logos/google_play_store-cb1f298b04afa7f74639a948d9b2e22e4aa6eea9486a2b0442c2cf9bdcda63e8.svg" />
</a>      <a target="_blank" rel="noopener" href="https://coingecko.app.link/footer-ios">
        <img loading="lazy" alt="Apple App Store Button" width="135" height="40" class="tw-mr-2" src="https://static.coingecko.com/s/coingecko_logos/apple_app_store-558245a688cc13737dfb861fd82b252d75d5afbaf343c06e3067a454675bbe05.svg" />
</a>    </div>
  </div>


  <!-- Disclaimer Notice -->
  <div class="container tw-my-6" id="footer-disclaimer">
    <a href="/en/disclaimer" data-view-component="true" class="!tw-font-bold tw-cursor-pointer tw-font-semibold tw-underline tw-text-slate-700 hover:tw-text-primary-500 hover:tw-underline dark:tw-text-slate-50 dark:hover:tw-text-primary-400">  IMPORTANT DISCLAIMER:</a>
    <div data-view-component="true" class="tw-inline tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  All content provided herein our website, hyperlinked sites, associated applications, forums, blogs, social media accounts and other platforms (“Site”) is for your general information only, procured from third party sources.  We make no warranties of any kind in relation to our content, including but not limited to accuracy and updatedness.  No part of the content that we provide constitutes financial advice, legal advice or any other form of advice meant for your specific reliance for any purpose.  Any use or reliance on our content is solely at your own risk and discretion.  You should conduct your own research, review, analyse and verify our content before relying on them.  Trading is a highly risky activity that can lead to major losses, please therefore consult your financial advisor before making any decision.  No content on our Site is meant to be a solicitation or offer.
</div>
  </div>

  <div data-view-component="true" class="tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
</div>

  </footer>
<!-- END: Footer Content -->


<!-- Modal content -->
    <div data-controller="settings-modal">
    <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="currency_selector" x-cloak="true" x-data="modalToggleable(&#39;currency_selector&#39;, 3000)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-start">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div id="currencySelector" class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-h-full tw-overflow-auto md:tw-max-w-4xl md:tw-max-h-[90vh] md:tw-h-fit md:tw-rounded-xl" x-cloak="true" x-show="currency_selector" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="currency_selector = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        <div data-view-component="true" class="tw-pt-3 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Select Currency
</div>
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
          <div class="tailwind-reset">
          <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input placeholder="Search" data-settings-modal-target="searchInput" data-action="input-&gt;settings-modal#handleSearchInput" type="text" data-view-component="true" class="!tw-h-10 gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
        </div>

          <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">Suggested Currencies</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
              <div data-iso-code="usd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;usd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  USD
</div>
                <span>US Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="idr" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;idr&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  IDR
</div>
                <span>Indonesian Rupiah</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="twd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;twd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  TWD
</div>
                <span>New Taiwan Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="eur" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;eur&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  EUR
</div>
                <span>Euro</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="krw" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;krw&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  KRW
</div>
                <span>South Korean Won</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="jpy" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;jpy&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  JPY
</div>
                <span>Japanese Yen</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="rub" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;rub&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  RUB
</div>
                <span>Russian Ruble</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="cny" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;cny&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CNY
</div>
                <span>Chinese Yuan</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>          </div>
          <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">Fiat Currencies</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
              <div data-iso-code="aed" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;aed&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  AED
</div>
                <span>United Arab Emirates Dirham</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="ars" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;ars&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ARS
</div>
                <span>Argentine Peso</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="aud" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;aud&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  AUD
</div>
                <span>Australian Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="bdt" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;bdt&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BDT
</div>
                <span>Bangladeshi Taka</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="bhd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;bhd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BHD
</div>
                <span>Bahraini Dinar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="bmd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;bmd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BMD
</div>
                <span>Bermudian Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="brl" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;brl&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BRL
</div>
                <span>Brazil Real</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="cad" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;cad&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CAD
</div>
                <span>Canadian Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="chf" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;chf&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CHF
</div>
                <span>Swiss Franc</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="clp" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;clp&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CLP
</div>
                <span>Chilean Peso</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="czk" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;czk&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CZK
</div>
                <span>Czech Koruna</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="dkk" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;dkk&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  DKK
</div>
                <span>Danish Krone</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="gbp" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;gbp&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  GBP
</div>
                <span>British Pound Sterling</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="gel" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;gel&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  GEL
</div>
                <span>Georgian Lari</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="hkd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;hkd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  HKD
</div>
                <span>Hong Kong Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="huf" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;huf&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  HUF
</div>
                <span>Hungarian Forint</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="ils" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;ils&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ILS
</div>
                <span>Israeli New Shekel</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="inr" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;inr&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  INR
</div>
                <span>Indian Rupee</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="kwd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;kwd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  KWD
</div>
                <span>Kuwaiti Dinar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="lkr" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;lkr&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  LKR
</div>
                <span>Sri Lankan Rupee</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="mmk" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;mmk&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  MMK
</div>
                <span>Burmese Kyat</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="mxn" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;mxn&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  MXN
</div>
                <span>Mexican Peso</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="myr" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;myr&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  MYR
</div>
                <span>Malaysian Ringgit</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="ngn" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;ngn&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  NGN
</div>
                <span>Nigerian Naira</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="nok" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;nok&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  NOK
</div>
                <span>Norwegian Krone</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="nzd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;nzd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  NZD
</div>
                <span>New Zealand Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="php" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;php&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  PHP
</div>
                <span>Philippine Peso</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="pkr" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;pkr&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  PKR
</div>
                <span>Pakistani Rupee</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="pln" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;pln&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  PLN
</div>
                <span>Polish Zloty</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="sar" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;sar&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SAR
</div>
                <span>Saudi Riyal</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="sek" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;sek&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SEK
</div>
                <span>Swedish Krona</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="sgd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;sgd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SGD
</div>
                <span>Singapore Dollar</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="thb" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;thb&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  THB
</div>
                <span>Thai Baht</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="try" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;try&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  TRY
</div>
                <span>Turkish Lira</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="uah" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;uah&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  UAH
</div>
                <span>Ukrainian hryvnia</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="vef" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;vef&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  VEF
</div>
                <span>Venezuelan bolívar fuerte</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="vnd" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;vnd&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  VND
</div>
                <span>Vietnamese đồng</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="zar" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;zar&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ZAR
</div>
                <span>South African Rand</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="xdr" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;xdr&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  XDR
</div>
                <span>IMF Special Drawing Rights</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>          </div>
          <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">Cryptocurrencies</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
              <div data-iso-code="btc" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;btc&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BTC
</div>
                <span>Bitcoin</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="eth" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;eth&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ETH
</div>
                <span>Ether</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="ltc" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;ltc&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  LTC
</div>
                <span>Litecoin</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="bch" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;bch&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BCH
</div>
                <span>Bitcoin Cash</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="bnb" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;bnb&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BNB
</div>
                <span>Binance Coin</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="eos" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;eos&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  EOS
</div>
                <span>EOS</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="xrp" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;xrp&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  XRP
</div>
                <span>XRP</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="xlm" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;xlm&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  XLM
</div>
                <span>Lumens</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="link" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;link&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  LINK
</div>
                <span>Chainlink</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="dot" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;dot&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  DOT
</div>
                <span>Polkadot</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="yfi" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;yfi&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  YFI
</div>
                <span>Yearn.finance</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>          </div>
          <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">Bitcoin Units</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
              <div data-iso-code="bits" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;bits&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BITS
</div>
                <span>Bits</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="sats" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;sats&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SATS
</div>
                <span>Satoshi</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>          </div>
          <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">Commodities</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
          <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
              <div data-iso-code="xag" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;xag&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  XAG
</div>
                <span>Silver - Troy Ounce</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>              <div data-iso-code="xau" data-action="click-&gt;analytics-tracker#trackEventFromTempProperties click-&gt;settings#changeCurrency" data-analytics-event-properties="{&quot;target_currency&quot;:&quot;xau&quot;}" data-view-component="true" class="tw-h-fit tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
                <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-self-start tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  XAU
</div>
                <span>Gold - Troy Ounce</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-fw tw-text-primary-500"></i>

</div>          </div>

</div>
      <div class="tw-text-center tw-pt-2 tw-mt-5 sm:tw-mt-6">        <div data-text="No results found" data-settings-modal-target="noSearchResults" data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-base tw-leading-6">
</div>
</div>
</div></div></div>  </div>

    <div data-controller="settings-modal">
    <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="language_selector" x-cloak="true" x-data="modalToggleable(&#39;language_selector&#39;, 2000)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-start">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-h-full tw-overflow-auto md:tw-max-w-4xl md:tw-max-h-[90vh] md:tw-h-fit md:tw-rounded-xl" x-cloak="true" x-show="language_selector" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="language_selector = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        <div data-view-component="true" class="tw-pt-3 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Select Language
</div>
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
          <div class="tailwind-reset">
          <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input placeholder="Search" data-settings-modal-target="searchInput" data-action="input-&gt;settings-modal#handleSearchInput" type="text" data-view-component="true" class="!tw-h-10 gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
        </div>


        <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">Popular Languages</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
        <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
            <div data-url="/en/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item tw-bg-gray-100 dark:tw-bg-moon-700 dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  EN
</div>
              <span>English</span>


  <i data-view-component="true" class="tw-ml-2 tw-ml-auto fas fa-check fa-fw tw-text-primary-500"></i>

</div>            <div data-url="/ru/%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  RU
</div>
              <span>Русский</span>


  
</div>            <div data-url="/de/b%C3%B6rsen/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  DE
</div>
              <span>Deutsch</span>


  
</div>            <div data-url="/pl/gie%C5%82dy/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  PL
</div>
              <span>język polski</span>


  
</div>            <div data-url="/es/intercambios/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ES
</div>
              <span>Español</span>


  
</div>            <div data-url="/vi/san_giao_dich/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  VI
</div>
              <span>Tiếng việt</span>


  
</div>            <div data-url="/fr/platesformes/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  FR
</div>
              <span>Français</span>


  
</div>            <div data-url="/pt/c%C3%A2mbios/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item  dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  PT
</div>
              <span>Português</span>


  
</div>        </div>


        <div data-view-component="true" class="tw-py-5 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  <span class="tw-shrink-0 tw-basis-auto">All Languages</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>
        <div class="tw-grid md:tw-grid-cols-2 lg:tw-grid-cols-4 tw-gap-4" data-settings-modal-target="itemGroup">
            <div data-url="/ar/%D8%B9%D9%85%D9%84%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D8%AA%D8%A8%D8%A7%D8%AF%D9%84/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  AR
</div>
              <span>العربية</span>


  
</div>            <div data-url="/bg/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  BG
</div>
              <span>български</span>


  
</div>            <div data-url="/cs/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  CS
</div>
              <span>čeština</span>


  
</div>            <div data-url="/da/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  DA
</div>
              <span>dansk</span>


  
</div>            <div data-url="/el/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  EL
</div>
              <span>Ελληνικά</span>


  
</div>            <div data-url="/fi/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  FI
</div>
              <span>suomen kieli</span>


  
</div>            <div data-url="/he/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  HE
</div>
              <span>עִבְרִית</span>


  
</div>            <div data-url="/hi/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  HI
</div>
              <span>हिंदी</span>


  
</div>            <div data-url="/hr/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  HR
</div>
              <span>hrvatski</span>


  
</div>            <div data-url="/hu/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  HU
</div>
              <span>Magyar nyelv</span>


  
</div>            <div data-url="/id/pertukaran/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ID
</div>
              <span>Bahasa Indonesia</span>


  
</div>            <div data-url="/it/cambi/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  IT
</div>
              <span>Italiano</span>


  
</div>            <div data-url="/ja/%E4%BA%A4%E6%8F%9B%E6%89%80/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  JA
</div>
              <span>日本語</span>


  
</div>            <div data-url="/ko/%EA%B1%B0%EB%9E%98%EC%86%8C/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  KO
</div>
              <span>한국어</span>


  
</div>            <div data-url="/lt/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  LT
</div>
              <span>lietuvių kalba</span>


  
</div>            <div data-url="/nl/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  NL
</div>
              <span>Nederlands</span>


  
</div>            <div data-url="/no/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  NO
</div>
              <span>norsk</span>


  
</div>            <div data-url="/ro/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  RO
</div>
              <span>Limba română</span>


  
</div>            <div data-url="/sk/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SK
</div>
              <span>slovenský jazyk</span>


  
</div>            <div data-url="/sl/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SL
</div>
              <span>slovenski jezik</span>


  
</div>            <div data-url="/sv/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  SV
</div>
              <span>Svenska</span>


  
</div>            <div data-url="/th/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%82%E0%B8%B2%E0%B8%A2/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  TH
</div>
              <span>ภาษาไทย</span>


  
</div>            <div data-url="/tr/borsalar/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  TR
</div>
              <span>Türkçe</span>


  
</div>            <div data-url="/uk/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  UK
</div>
              <span>украї́нська мо́ва</span>


  
</div>            <div data-url="/zh/exchanges/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ZH
</div>
              <span>简体中文</span>


  
</div>            <div data-url="/zh-tw/%E4%BA%A4%E6%98%93%E5%B9%B3%E5%8F%B0/xt" data-action="click-&gt;application#navigateToUrl" data-view-component="true" class="tw-cursor-pointer setting-item dark:tw-text-moon-100 dark:hover:tw-bg-moon-700 dark:hover:tw-text-moon-50 hover:tw-bg-gray-100 hover:tw-text-gray-900 tw-flex tw-items-center tw-py-3 tw-px-2 tw-rounded-lg tw-font-semibold tw-text-gray-700 tw-text-sm">
  
  
              <div data-view-component="true" class="tw-inline-block tw-mr-2 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  ZH-TW
</div>
              <span>繁體中文</span>


  
</div>        </div>

</div>
      <div class="tw-text-center tw-pt-2 tw-mt-5 sm:tw-mt-6">        <div data-text="No results found" data-settings-modal-target="noSearchResults" data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-base tw-leading-6">
</div>
</div>
</div></div></div>  </div>

  <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="auth_modal" x-cloak="true" x-data="modalToggleable(&#39;auth_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-start">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div id="auth-modal" class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="auth_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="auth_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
      <div x-data="{ activeTab: &#39;sign-in&#39; }" data-view-component="true">
  <nav class="tw-overflow-x-auto tw-flex tw-shadow-[inset_0_-1px_0_0_#EFF2F5] dark:tw-shadow-[inset_0_-1px_0_0_#212D3B]">
      <a data-auth-target="signInTab" @click="activeTab = &#39;sign-in&#39;" :class="{ selected: activeTab === &#39;sign-in&#39; }" id="tab-sign-in" data-view-component="true" class="tw-flex-1 tw-text-center gecko-tab-underline-item selected">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <span data-view-component="true">Login</span>
    

</span></a>

      <a data-auth-target="signUpTab" @click="activeTab = &#39;sign-up&#39;" :class="{ selected: activeTab === &#39;sign-up&#39; }" id="tab-sign-up" data-view-component="true" class="tw-flex-1 tw-text-center gecko-tab-underline-item">
  <span data-view-component="true" class="tw-font-semibold tw-text-sm tw-leading-5">
  
    
    <span data-view-component="true">Sign up</span>
    

</span></a>

  </nav>

  <div data-view-component="true">
      <div id="sign-in" x-show="activeTab === &#39;sign-in&#39;" data-view-component="true">
<div data-auth-target="signInTitle" data-view-component="true" class="tw-mt-6 tw-mb-2 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Log in
</div>
<div data-view-component="true" class="tw-mb-4 auth-modal-tnc tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium">
  
  By continuing, you agree to CoinGecko <a href="/en/terms" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Terms of Service</a> and acknowledge you’ve read our <a href="/en/privacy" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Privacy Policy</a>

</div>

<div class="tw-flex tw-flex-col tw-gap-y-4">
  <button data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;application#navigateToUrl" data-analytics-event="select_sign_in_method_cta" data-analytics-event-properties="{&quot;method&quot;:&quot;google&quot;,&quot;origin&quot;:&quot;login&quot;}" data-url="/omniauth/google_oauth2?locale=en" data-method="post" data-omniauth="true" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    
    <div data-view-component="true" class="tw-flex tw-py-1 tw-items-center tw-w-full tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
      <img width="20" height="20" loading="lazy" class="tw-flex-initial" src="https://static.coingecko.com/s/google-167c1e093ccfc014420e14da91325a1f70c91e592f58164fefe84603d2fde02e.svg" />
      <div class="tw-flex-1">
        Continue with Google
      </div>

</div>
</button>  <button data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;application#navigateToUrl" data-analytics-event="select_sign_in_method_cta" data-analytics-event-properties="{&quot;method&quot;:&quot;apple&quot;,&quot;origin&quot;:&quot;login&quot;}" data-url="/omniauth/apple?locale=en" data-method="post" data-omniauth="true" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    
    <div data-view-component="true" class="tw-flex tw-py-1 tw-items-center tw-w-full tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
      <img width="20" height="20" loading="lazy" class="tw-flex-initial dark:tw-hidden" src="https://static.coingecko.com/s/apple_black-6d9a519c69649e1a56774f4036ec552e412e73d5f9c2b0bab193732e47721533.svg" />
      <img width="20" height="20" loading="lazy" class="tw-flex-initial tw-hidden dark:tw-block" src="https://static.coingecko.com/s/apple_white-df0a614505190a8b2bc87fd16396160fed4680f62a69d5005cd2ae95562b2d2a.svg" />
      <div class="tw-flex-1">
        Continue with Apple
      </div>

</div>
</button></div>

<div data-view-component="true" class="tw-py-4 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
  <span class="tw-shrink-0 tw-basis-auto">or</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

<div x-data="{ show_email_input: false }">
  <div class="tw-flex tw-flex-col tw-gap-y-4">
    <button @click="show_email_input = true" x-show="!show_email_input" data-action="click-&gt;auth#focusLogInEmailInput" type="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    
      <div data-view-component="true" class="tw-flex tw-py-1 tw-items-center tw-w-full tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
        <div class="tw-flex-1">
          Continue with email
        </div>

</div>
</button>  </div>

  <div x-show="show_email_input">
    <form data-controller="refresh-csrf-token" data-csrf-meta-target="form" data-refresh-csrf-token-target="form" class="new_user" id="new_user" action="/account/sign_in?locale=en" accept-charset="UTF-8" method="post">
        <input value="" autocomplete="off" type="hidden" name="user[mixpanel_device_id]" id="user_mixpanel_device_id" />
  <input value="{}" autocomplete="off" type="hidden" name="user[utm_json]" id="user_utm_json" />


      <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mb-4">
        <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input name="user[email]" id="user_email" placeholder="Enter your email address" data-auth-target="logInEmailInput" value="" type="email" data-view-component="true" class="!tw-h-12 tw-text-base md:tw-text-sm gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
        <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input name="user[password]" id="user_password" placeholder="Enter your password" type="password" data-view-component="true" class="!tw-h-12 tw-text-base md:tw-text-sm gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
      </div>
      <div class="tw-flex tw-justify-between tw-items-center tw-mb-5">
          <input name="user[remember_me]" type="hidden" value="0" autocomplete="off" /><label for="user_remember_me" data-view-component="true" class="tw-flex tw-items-start !tw-mb-0 tw-block tw-text-sm tw-font-medium tw-text-gray-900 dark:tw-text-moon-50 has-[:disabled]:tw-opacity-50 has-[:disabled]:tw-pointer-events-none gecko-checkbox">
  <input id="user_remember_me" name="user[remember_me]" value="1" checked="checked" type="checkbox" class="tw-form-checkbox tw-h-4 tw-w-4 tw-mt-0.5 !tw-mr-2 !tw-border !tw-border-gray-300 !tw-text-primary-500 !tw-rounded focus:tw-ring-primary-600 dark:!tw-border-moon-600 dark:tw-bg-transparent dark:tw-ring-offset-moon-900 checked:dark:tw-bg-primary-600 checked:!tw-border-primary-500 checked:dark:!tw-border-primary-600" />

  <div>
    <div data-view-component="true" class="gecko-checkbox-label">Remember me</div>
    
    <div x-ref="error" data-view-component="true" class="tw-mt-1 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  </div>
</label>        <span data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;auth#openResetPasswordModal" data-analytics-event="select_forgot_password_cta" data-view-component="true" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Forgot your password?</span>
      </div>
      <div data-action="click->analytics-tracker#unconditionalTrackEvent" data-analytics-event="select_sign_in_method_cta" data-analytics-event-properties="{&quot;method&quot;:&quot;email&quot;,&quot;origin&quot;:&quot;login&quot;}">
        <button data-action="click-&gt;refresh-csrf-token#submit" type="submit" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Login

</div></button>
      </div>
</form>
    <div data-view-component="true" class="tw-py-4 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

    <div data-view-component="true" class="tw-text-center tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  
      Didn&#39;t receive confirmation instructions?
      <div data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;auth#openResendConfirmationModal" data-analytics-event="select_resend_confirmation_email_cta" data-view-component="true" class="tw-text-center !tw-text-sm tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Resend confirmation instructions</div>

</div>  </div>
</div>
</div>
      <div id="sign-up" x-cloak="" x-show="activeTab === &#39;sign-up&#39;" data-view-component="true">
<div data-auth-target="signUpTitle" data-view-component="true" class="tw-mt-6 tw-mb-2 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Sign up
</div>
<div data-view-component="true" class="tw-mb-4 auth-modal-tnc tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium">
  
  By continuing, you agree to CoinGecko <a href="/en/terms" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Terms of Service</a> and acknowledge you’ve read our <a href="/en/privacy" class="tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Privacy Policy</a>

</div>


<form data-controller="captcha" data-csrf-meta-target="form" class="new_user" id="new_user" action="/account?locale=en" accept-charset="UTF-8" method="post">
    <input value="" autocomplete="off" type="hidden" name="user[mixpanel_device_id]" id="user_mixpanel_device_id" />
  <input value="{}" autocomplete="off" type="hidden" name="user[utm_json]" id="user_utm_json" />


  <div class="tw-flex tw-flex-col tw-gap-y-4">
    <button data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;application#navigateToUrl" data-analytics-event="select_sign_in_method_cta" data-analytics-event-properties="{&quot;method&quot;:&quot;google&quot;,&quot;origin&quot;:&quot;sign_up&quot;}" data-url="/omniauth/google_oauth2?locale=en" data-method="post" data-omniauth="true" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    
      <div data-view-component="true" class="tw-flex tw-py-1 tw-items-center tw-w-full tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
        <img width="20" height="20" loading="lazy" class="tw-flex-initial" src="https://static.coingecko.com/s/google-167c1e093ccfc014420e14da91325a1f70c91e592f58164fefe84603d2fde02e.svg" />
        <div class="tw-flex-1">
          Continue with Google
        </div>

</div>
</button>
    <button data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;application#navigateToUrl" data-analytics-event="select_sign_in_method_cta" data-analytics-event-properties="{&quot;method&quot;:&quot;apple&quot;,&quot;origin&quot;:&quot;sign_up&quot;}" data-url="/omniauth/apple?locale=en" data-method="post" data-omniauth="true" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    
      <div data-view-component="true" class="tw-flex tw-py-1 tw-items-center tw-w-full tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
        <img width="20" height="20" loading="lazy" class="tw-flex-initial dark:tw-hidden" src="https://static.coingecko.com/s/apple_black-6d9a519c69649e1a56774f4036ec552e412e73d5f9c2b0bab193732e47721533.svg" />
        <img width="20" height="20" loading="lazy" class="tw-flex-initial tw-hidden dark:tw-block" src="https://static.coingecko.com/s/apple_white-df0a614505190a8b2bc87fd16396160fed4680f62a69d5005cd2ae95562b2d2a.svg" />
        <div class="tw-flex-1">
          Continue with Apple
        </div>

</div>
</button>  </div>

  <div data-view-component="true" class="tw-py-4 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
  <span class="tw-shrink-0 tw-basis-auto">or</span>
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

  <div x-data="{ show_email_input: false }">
    <div class="tw-flex tw-flex-col tw-gap-y-4">
      <button @click="show_email_input = true" x-show="!show_email_input" data-action="click-&gt;auth#focusSignUpEmailInput" type="button" data-view-component="true" class="tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-flex tw-w-full">

    
        <div data-view-component="true" class="tw-flex tw-py-1 tw-items-center tw-w-full tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  
          <div class="tw-flex-1">
            Continue with email
          </div>

</div>
</button>    </div>

    <div x-show="show_email_input">
      <div class="tw-flex tw-flex-col tw-gap-y-4">
        <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input name="user[email]" id="user_email" placeholder="Enter your email address" autocomplete="email" data-action="focus-&gt;captcha#loadCaptcha" data-auth-target="signUpEmailInput" value="" type="email" data-view-component="true" class="!tw-h-12 tw-text-base md:tw-text-sm gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
        <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input name="user[password]" id="user_password" placeholder="Enter your password" autocomplete="new-password" data-action="focus-&gt;captcha#loadCaptcha input-&gt;auth#validate focus-&gt;auth#validate" data-auth-target="signUpPassword" type="password" data-view-component="true" class="!tw-h-12 tw-text-base md:tw-text-sm gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
      </div>
      <div class="tw-flex tw-flex-col tw-gap-y-4 tw-mt-4">
        <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium">
  Password must contain at least 8 characters including 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character

</div>

        <div id="sign-up-captcha" data-sitekey="d7b4358f-5390-46d4-a479-eb9a1fa28033" data-captcha-target="captchaForm" class="tw-mx-auto tw-hidden"></div>
      </div>
      <div class="tw-mt-5">
        <button data-auth-target="signUpSubmit" data-captcha-target="submit" data-action="click-&gt;analytics-tracker#unconditionalTrackEvent" data-analytics-event="select_sign_in_method_cta" data-analytics-event-properties="{&quot;method&quot;:&quot;email&quot;,&quot;origin&quot;:&quot;sign_up&quot;}" disabled="disabled" type="submit" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Sign up

</div></button>
      </div>

      <div data-view-component="true" class="tw-py-4 tw-flex tw-gap-x-2 tw-items-center tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm">
  
  
  <div class="tw-w-full tw-border-t tw-border-gray-200 dark:tw-border-moon-700"></div>
</div>

      <div data-view-component="true" class="!tw-text-center tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  
        Didn&#39;t receive confirmation instructions?
        <div data-action="click-&gt;analytics-tracker#unconditionalTrackEvent click-&gt;auth#openResendConfirmationModal" data-analytics-event="select_resend_confirmation_email_cta" data-view-component="true" class="tw-text-center !tw-text-sm tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400">  Resend confirmation instructions</div>

</div>    </div>
  </div>
</form></div>
</div></div>
</div>
      
</div></div></div>
<div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="reset_password_modal" x-cloak="true" x-data="modalToggleable(&#39;reset_password_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-center">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="reset_password_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="reset_password_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
      <div data-auth-target="resetPasswordContent">
      <div data-view-component="true" class="tw-mb-2 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Forgot your password?
</div>
<div data-view-component="true" class="tw-mb-5 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  You will receive an email with instructions on how to reset your password in a few minutes.
</div>

<form data-controller="captcha" data-csrf-meta-target="form" class="new_user" id="new_user" action="/account/password" accept-charset="UTF-8" method="post">
  <div class="tw-flex tw-flex-col tw-gap-y-5">
    <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input name="user[email]" id="user_email" label="Email" data-action="focus-&gt;captcha#loadCaptcha" value="" type="email" data-view-component="true" class="!tw-h-12 tw-text-base md:tw-text-sm gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>

    <div id="reset-password-captcha" data-sitekey="12bff373-21ea-4374-9880-ad11db5eb04a" data-captcha-target="captchaForm" class="tw-mx-auto tw-hidden"></div>

    <button data-captcha-target="submit resetPassword" data-action="click-&gt;analytics-tracker#unconditionalTrackEvent" data-analytics-event="select_reset_password_cta" disabled="disabled" type="submit" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Send me reset password instructions

</div></button>
  </div>
</form>
    </div>

</div>
      
</div></div></div>
<div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="resend_confirmation_modal" x-cloak="true" x-data="modalToggleable(&#39;resend_confirmation_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-center">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="resend_confirmation_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="resend_confirmation_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
      <div data-auth-target="resendConfirmationContent">
      <div data-view-component="true" class="tw-mb-2 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Resend confirmation instructions
</div>
<div data-view-component="true" class="tw-mb-5 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  You will receive an email with instructions for how to confirm your email address in a few minutes.
</div>

<form data-csrf-meta-target="form" class="new_user" id="new_user" action="/account/confirmation" accept-charset="UTF-8" method="post">
  <div class="tw-flex tw-flex-col tw-gap-y-5">
    <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input name="user[email]" id="user_email" label="Email" value="" type="email" data-view-component="true" class="!tw-h-12 tw-text-base md:tw-text-sm gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
    <button type="submit" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Resend confirmation instructions

</div></button>
  </div>
</form>
    </div>

</div>
      
</div></div></div>
  <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="get_app_modal" x-cloak="true" x-data="modalToggleable(&#39;get_app_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-center">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="get_app_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="get_app_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        <div data-view-component="true" class="tw-text-center tw-pt-3 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
  Get the CoinGecko app.
</div>
      </div>
      <div data-view-component="true" class="!tw-pt-2 tw-text-center tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
      Scan this QR code to download the app now
    <img alt="App QR Code" class="tw-block tw-mx-auto tw-my-4" src="https://static.coingecko.com/s/landing_pages/mobile_app_qr_code-503a3393ccc355a8c41ea1a4026c31db469665b66c47847b347e2447c80feea3.svg" width="160" height="160" />
    Or check it out in the app stores
    <div class="tw-mt-2">
      <a target="_blank" rel="noopener" href="https://coingecko.app.link/footer-android">
        <img alt="Google Play Store Button" width="135" height="40" class="tw-mr-2" src="https://static.coingecko.com/s/coingecko_logos/google_play_store-cb1f298b04afa7f74639a948d9b2e22e4aa6eea9486a2b0442c2cf9bdcda63e8.svg" />
</a>      <a target="_blank" rel="noopener" href="https://coingecko.app.link/footer-ios">
        <img alt="Apple App Store Button" width="135" height="40" src="https://static.coingecko.com/s/coingecko_logos/apple_app_store-558245a688cc13737dfb861fd82b252d75d5afbaf343c06e3067a454675bbe05.svg" />
</a></div>
</div>
      
</div></div></div>


  <div x-data>
    <div class="tw-fixed tw-inset-0 tw-overflow-y-auto gecko-modal" style="z-index: 0;" x-show="dynamic_modal" x-cloak="true" x-data="modalToggleable(&#39;dynamic_modal&#39;, 50)" x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform" x-transition:enter-end="tw-opacity-100 tw-transform" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform">
  <div class="tw-flex tw-justify-center tw-min-h-screen md:tw-py-4 tw-items-center">
    <!-- Modal backdrop -->
    <div class="tw-fixed tw-inset-0 tw-bg-gray-900/60 dark:tw-bg-black/60 tw-transition-opacity" aria-hidden="true"></div>

    <!-- Modal panel -->
    <div class="tw-bg-white dark:tw-bg-moon-800 tw-inline-block tw-align-bottom tw-px-6 tw-pb-6 tw-w-full tw-text-left tw-shadow-xl tw-transform tw-transition-all sm:tw-align-middle tw-max-w-lg tw-overflow-hidden tw-rounded-xl" x-cloak="true" x-show="dynamic_modal" @mousedown.away="handleClickAway($el)" x-transition:enter="tw-transition tw-ease-out tw-duration-300" x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5" x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0" x-transition:leave="tw-transition tw-ease-in tw-duration-300" x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5">
      <div class="tw-grid tw-grid-cols-10 tw-justify-between tw-items-center tw-pt-6 ">
        <div class="tw-sticky tw-top-0 tw-bg-white dark:tw-bg-moon-800 tw-text-2xl tw-col-span-1">
          <i @click="dynamic_modal = false" data-view-component="true" class="tw-text-gray-400 hover:tw-text-gray-500 dark:tw-text-moon-500 dark:hover:tw-text-moon-400 tw-cursor-pointer far fa-times"></i>

        </div>

        

        <div class="tw-col-span-1 tw-flex tw-justify-end">
          
        </div>
      </div>

      <div class="tw-text-left">
        <div x-text="$store.modals.dynamicModal.title" x-show="$store.modals.dynamicModal.title" data-view-component="true" class="tw-pt-3 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7">
</div>
      </div>
      <div data-view-component="true" class="tw-pt-3 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
          <div x-show="$store.modals.dynamicModal.content" x-html="$store.modals.dynamicModal.content" data-view-component="true" class="tw-mb-4 tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
</div>
        <div x-show="$store.modals.dynamicModal.inputField">
          <div x-data="input" x-on:gp-input-error="showHideInputError($event)" data-view-component="true" class="tw-px-0.5">
  


  <div id="dynamic-modal-input_container" x-ref="container" data-view-component="true" class="gecko-input-group">
    

      <input :placeholder="$store.modals.dynamicModal.inputPlaceholder" @input="$store.modals.dynamicModal.inputValue = $event.target.value;" id="dynamic-modal-input" type="text" data-view-component="true" class="gecko-input"></input>

    
</div>

  <div x-ref="error" data-view-component="true" class="tw-mt-2 !tw-font-semibold !tw-text-danger-500 tw-hidden tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-semibold">
</div>
  
</div>
        </div>

        <div class="tw-mt-6 tw-flex tw-gap-x-2">
          <button @click="$store.modals.dynamicModal._cancel" x-show="$store.modals.dynamicModal.cancelText" type="button" data-view-component="true" class="tw-bg-white dark:tw-bg-moon-800 !tw-border-t-2 !tw-border-x-2 !tw-border-slate-300 dark:!tw-border-moon-500 tw-shadow-secondaryShadow dark:tw-shadow-secondaryShadowDark !tw-mb-1 hover:tw-bg-slate-100 dark:hover:tw-bg-moon-700 hover:tw-shadow-secondaryHover dark:hover:tw-shadow-secondaryHoverDark active:!tw-shadow-secondaryActive dark:active:!tw-shadow-secondaryActiveDark tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-slate-900 hover:tw-text-slate-900 focus:tw-text-slate-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      
            <span x-text="$store.modals.dynamicModal.cancelText"></span>


</div></button>          <button @click="$store.modals.dynamicModal._confirm" x-show="$store.modals.dynamicModal.confirmText" type="button" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      
            <span x-text="$store.modals.dynamicModal.confirmText"></span>


</div></button>          <button @click="$store.modals.dynamicModal._confirm" x-show="$store.modals.dynamicModal.dangerText" type="button" data-view-component="true" class="tw-bg-danger-500 dark:tw-bg-danger-400 tw-shadow-dangerShadow !tw-mb-1 hover:tw-bg-danger-600 dark:hover:tw-bg-danger-300 hover:tw-shadow-dangerHover active:!tw-shadow-dangerActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-danger-900 dark:hover:tw-text-danger-900 dark:focus:tw-text-danger-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      
            <span x-text="$store.modals.dynamicModal.dangerText"></span>


</div></button>        </div>

</div>
      
</div></div></div>  </div>


  <div data-controller="app-flyer" data-app-flyer-target="banner" class="tw-fixed tw-bottom-0 tw-w-screen tw-z-50 tw-hidden tailwind-reset">
    <div class="tw-p-4 tw-bg-white tw-border-t tw-border-gray-200 tw-rounded-t-xl dark:tw-bg-moon-800 dark:tw-border-moon-700 tw-flex tw-gap-x-2">
      <div data-action="click-&gt;app-flyer#dismiss" data-view-component="true" class="tw-flex tw-items-center tw-cursor-pointer tw-px-0.5 tw-text-gray-700 dark:tw-text-moon-100 tw-font-medium tw-text-sm tw-leading-5">
  
        <i data-view-component="true" class="far fa-close"></i>


</div>
      <img loading="lazy" alt="coingecko" class="tw-h-10 tw-w-10 tw-mr-1" src="https://static.coingecko.com/s/gecko-65456030ba03df0f83f96e18d0c8449485c1a61dbdeeb733ca69164982489d0e.svg" />

      <div class="tw-flex-1 tw-flex tw-justify-between tw-items-center">
        <div>
          <div data-view-component="true" class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5">
  Continue in app
</div>
          <div data-view-component="true" class="tw-font-normal tw-text-gray-500 dark:tw-text-moon-200 tw-text-sm tw-leading-5">
  Track prices in real-time
</div>
        </div>
        <div>
          <a href="https://coingecko.app.link/lTInCXLGz4" role="button" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-2.5 tw-py-1.5 tw-inline-flex">

    <div data-view-component="true" class="tw-text-xs tw-leading-4 tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold">
  
      Open App

</div></a>
        </div>
      </div>
    </div>
  </div>



<!-- START: Floating Content -->
<button onclick="window.scrollTo({ top: 0, behavior: &#39;smooth&#39; })" type="button" data-view-component="true" class="tw-fixed tw-bottom-0 tw-right-0 tw-m-5 tw-z-10 tw-bg-gray-200 dark:tw-bg-moon-700 hover:tw-bg-gray-300 dark:hover:tw-bg-moon-600 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-4 tw-py-2 tw-inline-flex">

    <div data-view-component="true" class="tw-text-gray-900 hover:tw-text-gray-900 focus:tw-text-gray-900 dark:tw-text-moon-50 dark:hover:tw-text-moon-50 dark:focus:tw-text-moon-50 tw-font-semibold tw-text-sm tw-leading-5">
  
      
  <i data-view-component="true" class="fas fa-arrow-to-top"></i>



</div></button>
<div class="tw-w-screen tw-h-[100dvh] tw-pointer-events-none tw-gap-y-4 tw-z-[20000] tw-fixed tw-inset-0 tw-flex tw-flex-col tw-justify-end sm:tw-justify-start tw-items-center sm:tw-items-end tw-p-6"
     data-controller="toaster" data-toaster-target="content" aria-live="assertive">
</div>

  <div data-controller="gecko-float-modal" data-gecko-float-modal-version="13" x-data="{ open: false }">
  <div id="geckoFloat" data-gecko-float-modal-target="geckoButton" class="tw-hidden tw-fixed tw-z-40 md:tw-z-[1200] tw-right-0 tw-mb-8 tw-bottom-6">
    <div class="tw-static tw-z-10 tw-mr-6 tw-mb-2" x-cloak x-show="!open" @click="open = true" data-action="click->gecko-float-modal#clickGeckoGuide">
      <div data-gecko-float-modal-target="geckoButtonPing" class="tw-invisible tw-absolute -tw-top-1 tw-right-1 tw-rounded-full tw-bg-primary-200 tw-opacity-50 tw-flex tw-p-5 tw-relative"></div>
      <div class="tw-absolute tw-top-0.5 tw-left-0.5 tw-cursor-pointer tw-z-20" >
        <img fetchpriority="high" class="tw-w-[41px] tw-h-[41px] dark:tw-border-solid dark:tw-border-[3px] dark:tw-border-[#78E4F4] tw-rounded-md tw-filter tw-drop-shadow-geckoguide" src="https://static.coingecko.com/s/geckocon_2024/gecko_float-64de18d5027eec69efa01c6ca54f5973b37516dd8a017d5d81145300110a2f70.png" />
      </div>
    </div>
    <div class="tw-hidden md:tw-flex tw-justify-center tw-items-center tw-cursor-pointer tw-z-[1200] tw-w-[41px] tw-h-[41px] tw-mr-6 tw-mb-2 tw-top-0 tw-bg-primary-500 tw-rounded-full" x-cloak x-show="open" @click="open = false" data-action="click->gecko-float-modal#submitHideDialogForm">
      <span class="tw-text-2xl tw-text-white tw-pt-0.5"><i class="far fa-times"></i></span>
    </div>
  </div>
  <div
    x-cloak
    x-show="open"
    class="tw-fixed tw-z-[1190] tw-inset-0 tw-bg-black tw-bg-opacity-75 tw-overflow-y-auto tw-h-full tw-w-full"
    x-transition:enter="tw-transition tw-transition-opacity tw-ease-out tw-duration-300"
    x-transition:enter-start="tw-opacity-0 tw-transform "
    x-transition:enter-end="tw-opacity-100 tw-transform "
    x-transition:leave="tw-transition tw-ease-in tw-duration-300"
    x-transition:leave-end="tw-opacity-0 tw-transform "
    id="my-modal"
    data-action="click->gecko-float-modal#submitHideDialogForm"
  >
  </div>

  <!--modal content-->
  <div
    x-cloak
    x-show="open"
    class="tw-fixed tw-z-[1200] gecko-guide-dialog-position md:tw-bottom-40 tw-mr-3 tw-top-0 md:tw-top-[unset] md:tw-right-2 md:tw-mt-4 tw-border tw-w-full md:tw-w-auto tw-h-full md:tw-h-auto md:tw-w-96 md:tw-shadow-lg md:tw-rounded-md tw-bg-white dark:tw-bg-dark-10 dark:tw-text-white tw-overflow-hidden tw-overflow-y-auto"
    x-transition:enter="tw-transition tw-ease-out tw-duration-300"
    x-transition:enter-start="tw-opacity-0 tw-transform tw--translate-y-5"
    x-transition:enter-end="tw-opacity-100 tw-transform tw-translate-y-0"
    x-transition:leave="tw-transition tw-ease-in tw-duration-300"
    x-transition:leave-end="tw-opacity-0 tw-transform tw--translate-y-5"
    @click.away="open = false"
  >
    <div class="tw-mt-6 tw-ml-6 md:tw-hidden">
      <span @click="open = false" data-action="click->gecko-float-modal#submitHideDialogForm" class="tw-text-2xl tw-text-gray-400 dark:tw-text-white"><i class="far fa-times"></i></span>
    </div>
    <div class="tw-grid tw-px-6 tw-py-2 tw-place-items-center">
      <a target="_blank" href="https://landing.coingecko.com/geckocon-2024">
        <img loading="lazy" class="tw-w-[340px] tw-h-40" src="https://static.coingecko.com/s/geckocon_2024/banner-d11b6f133ba12070de12ff1699627f63e6e8b5703a412c680536e4bde943f21a.png" />
</a>    </div>

    <div class="tw-grid tw-px-6 tw-py-3 tw-place-items-center">
      <span data-view-component="true" class="tw-w-[340px] tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-base tw-leading-6">
  Join us at our first hybrid conference on 11 Nov 2024. Final chance to grab tickets at 25% off—don’t wait!
</span>
    </div>

    <div class="tw-grid tw-px-6 tw-pt-2 tw-pb-4">
      <a target="_blank" href="https://bit.ly/46Em5uN" role="button" data-view-component="true" class="tw-bg-primary-500 dark:tw-bg-primary-400 tw-shadow-primaryShadow !tw-mb-1 hover:tw-bg-primary-600 dark:hover:tw-bg-primary-300 hover:tw-shadow-primaryHover active:!tw-shadow-primaryActive tw-transition-all tw-duration-150 active:tw-translate-y-2 tw-items-center tw-justify-center tw-font-semibold tw-text-inline tw-rounded-lg tw-select-none focus:tw-outline-none tw-px-6 tw-py-3.5 tw-flex tw-w-full">

    <div data-view-component="true" class="tw-text-white hover:tw-text-white focus:tw-text-white dark:tw-text-primary-900 dark:hover:tw-text-primary-900 dark:focus:tw-text-primary-900 tw-font-semibold tw-text-sm tw-leading-5">
  
      Find out more

</div></a>
    </div>
    <hr class="md:tw-my-0 dark:tw-border-white dark:tw-border-opacity-12">

    <form class="tw-px-5 tw-py-4 tw-inline-block tw-align-baseline tw-leading-3" action="index.html">
      <span class="tw-mt-2">
        <input id="hideGeckoGuideCheckbox" type="checkbox" classes="tw-w-4 tw-h-4" data-gecko-float-modal-target="hideDialogCheckbox" >
      </span>
      <label for="hideGeckoGuideCheckbox" class="tw-text-sm tw-ml-2 tw-inline-block tw-leading-3">Do Not Show 7 Days</label><br>
    </form>
  </div>
</div>


<!-- END: Floating Content -->


<!-- START: Stimulus JS Scripts -->
<script src="https://static.coingecko.com/s/application_v2-1851a70c6dcd7318a6cc1b93f0c221635852d0bcc7cde2224ae4ac379e06c8e4.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/runtime~i18n-19f21d2ffc99917313aa.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/vendors~i18n-8c8793e29e7471b8c144.chunk.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/i18n-e3bdd92bd4309b73baae.chunk.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/runtime~translations/en-6a71d8e6b7a4abfd7ba4.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/translations/en-1c9b18440cf969d0603f.chunk.js" defer="defer"></script>

<script src="https://static.coingecko.com/packs/js/runtime~v2/application-d6a34ca941b6a6636d95.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/vendors~gecko_primer~v2/application~v2/errors~v2/pages/account~v2/pages/all_coins~v2/pages/candy~v2/~4677dea5-5aad1f3bca4b946a159e.chunk.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/vendors~alpine~v2/application~v2/pages/coins~v2/pages/exchanges~v2/pages/global_charts~v2/pages/nft~~d8c8c671-279ea1890152581ff790.chunk.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/v2/application-cc53f236c8d8387ab539.chunk.js" defer="defer"></script>









<script src="https://static.coingecko.com/packs/js/runtime~v2/pages/exchanges-324faea7ac6f860912cb.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/vendors~gecko_primer~v2/application~v2/errors~v2/pages/account~v2/pages/all_coins~v2/pages/candy~v2/~4677dea5-5aad1f3bca4b946a159e.chunk.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/vendors~alpine~v2/application~v2/pages/coins~v2/pages/exchanges~v2/pages/global_charts~v2/pages/nft~~d8c8c671-279ea1890152581ff790.chunk.js" defer="defer"></script>
<script src="https://static.coingecko.com/packs/js/v2/pages/exchanges-569dbe7b18534c8144ef.chunk.js" defer="defer"></script>





















<!-- END: Stimulus JS Scripts -->

<img src = "https://cloudcdn-img.com/static/752c02be/spacer.gif" referrerpolicy="no-referrer-when-downgrade" style = "opacity: 0; width: 1px; height: 1px;"/>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"rayId":"8c94e0725edfce2d","serverTiming":{"name":{"cfExtPri":true,"cfL4":true}},"version":"2024.8.0","token":"ca697cea96514f4093039c105354b47b"}' crossorigin="anonymous"></script>
</body>
</html>

'''
soup = BeautifulSoup(html, 'html.parser')
# tags = soup.find_all('div', {'class': 'tw-block 2lg:tw-inline tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium'})

# for tag in tags:
#     print(tag.text.strip())
# tags = soup.find_all('a', {'class': "tw-cursor-pointer tw-font-semibold tw-no-underline tw-text-slate-700 hover:tw-text-primary-500 dark:tw-text-moon-50 dark:hover:tw-text-primary-400"})
tags = soup.find_all('div', {'class': "tw-flex tw-gap-x-2 tw-whitespace-nowrap"})
print(len(tags))
for tag in tags:
    print(tag.text.strip())
    

a = '''BTC
ETH
USDT
BNB
SOL
USDC
XRP
STETH
DOGE
TON
ADA
TRX
AVAX
WSTETH
SHIB
WBTC
LINK
WETH
BCH
DOT
NEAR
UNI
DAI
LEO
LTC
SUI
ICP
WEETH
FET
APT
KAS
TAO
PEPE
POL
STX
XMR
ETC
XLM
FDUSD
IMX
USDE
RENDER
OKB
AAVE
FIL
CRO
ARB
HBAR
INJ
WIF
MNT
OP
VET
FTM
ATOM
RUNE
GRT
SEI
WBT
WETH
THETA
AR
FLOKI
RETH
BONK
MKR
BGB
TIA
SOLVBTC
PYTH
METH
JUP
HNT
MATIC
ALGO
ONDO
QNT
GT
JASMY
LDO
OM
POPCAT
BSV
CORE
WLD
EZETH
BRETT
KCS
FLOW
BEAM
BTT
GALA
EETH
NOT
STRK
MSOL
ORDI
EOS
EGLD
AXS
'''

b = '''BTC/USDT
ETH/USDT
NEIRO/USDT
XT/USDT
ETH/USDC
DOGE/USDT
SEI/USDT
SOL/USDT
HMSTR/USDT
BNB/USDT
CAT/USDT
AAVE/USDT
INJ/USDT
WIF/USDT
PEOPLE/USDT
STRK/USDT
STX/USDT
TAO/USDT
XRP/USDT
MOODENG/USDT
FTM/USDT
NEAR/USDT
WLD/USDT
ARB/USDT
FIDA/USDT
SAGA/USDT
CHZ/USDT
TRX/USDT
LINK/USDT
MOTHER/USDT
AVAX/USDT
PHB/USDT
ETH/XTUSD
EDLC/USDT
FET/USDT
USDC/USDT
LTC/USDT
ADA/USDT
FLOKI/USDT
MOG/USDT
AR/USDT
XMR/USDT
CELO/USDT
NOT/USDT
BONK/USDT
CORE/USDT
NEIRO/USDT
POPCAT/USDT
UNI/USDT
FIL/USDT
CRV/USDT
ATOM/USDT
SUPER/USDT
PENDLE/USDT
BABYBONK/USDT
ETHDYDX/USDT
BOME/USDT
ARKM/USDT
RATS/USDT
GMT/USDT
HOOK/USDT
SLF/USDT
BCH/USDT
BRETT/USDT
KAVA/USDT
ICE/USDT
APT/USDT
ARPA/USDT
LOKA/USDT
SHRAP/USDT
OM/USDT
MEW/USDT
BLUR/USDT
AUCTION/USDT
BTC/USDC
ORDI/USDT
ENA/USDT
SMH/USDT
TON/USDT
GALA/USDT
MINA/USDT
DOGS/USDT
AXL/USDT
VET/USDT
SATS/USDT
BILLY/USDT
IMX/USDT
XLM/USDT
ROSE/USDT
LUNA/USDT
MANTA/USDT
COTI/USDT
AGI/USDT
ETHFI/USDT
CTK/USDT
CKB/USDT
ZERO/USDT
SNX/USDT
EDOGE/USDT
'''

a = a.strip('\n').split('\n')
xt = b.strip('\n').split('\n')
print(len(a), len(xt))
xt_coins = []
for coin in xt:
    coinname = coin.split('/')[0]
    xt_coins.append(coinname)
print(len(xt_coins))
xt_not_in_a = []
a_not_in_xt = []
duplicate = []
for coin in xt:
    if coin.split('/')[0] in a:
        duplicate.append(coin)
    else:
        xt_not_in_a.append(coin)

for coin in a:
    if coin not in xt_coins:
    #     print(coin)
    # else:
        a_not_in_xt.append(coin)

print('')
for it in xt_not_in_a:
    print(it)
for it in a_not_in_xt:
    print(it+'/USDT')
for it in duplicate:
    print(it)
# print([it for it in xt_not_in_a])
# print([it for it in a_not_in_xt])
# print([it for it in duplicate])
print(len(duplicate), len(xt_not_in_a), len(a_not_in_xt))

print()
