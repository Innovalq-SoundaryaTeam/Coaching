/*!
 * LS Academy — core front-end JS
 * Handles: theme (dark/light) toggle, RTL toggle, navbar scroll state,
 * mobile dashboard sidebar, scroll-reveal, back-to-top, blog filter/search,
 * FAQ/testimonial helpers, coming-soon countdown, simple form-validation UX.
 * No build step required — vanilla JS only.
 */
(function () {
  "use strict";

  var STORAGE_THEME = "ap-theme";
  var STORAGE_DIR = "ap-dir";
  var root = document.documentElement;

  /* ---------------------------------------------------------------------
   * Theme (dark / light)
   * ------------------------------------------------------------------- */
  function getPreferredTheme() {
    var stored = safeGet(STORAGE_THEME);
    if (stored) return stored;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(theme) {
    root.setAttribute("data-bs-theme", theme);
    document.querySelectorAll("[data-theme-icon]").forEach(function (el) {
      el.className = theme === "dark" ? "bi bi-sun" : "bi bi-moon-stars";
    });
    document.querySelectorAll("[data-theme-label]").forEach(function (el) {
      el.textContent = theme === "dark" ? "Light mode" : "Dark mode";
    });
  }

  function toggleTheme() {
    var current = root.getAttribute("data-bs-theme") === "dark" ? "dark" : "light";
    var next = current === "dark" ? "light" : "dark";
    applyTheme(next);
    safeSet(STORAGE_THEME, next);
  }

  /* ---------------------------------------------------------------------
   * RTL / LTR
   * ------------------------------------------------------------------- */
  function applyDir(dir) {
    root.setAttribute("dir", dir);
    root.setAttribute("lang", dir === "rtl" ? "ar" : "en");
    // Swap the vendored Bootstrap stylesheet for its RTL build (same folder, different filename)
    // so RTL works fully offline without depending on a CDN.
    var bsCss = document.getElementById("bootstrap-css");
    if (bsCss) {
      bsCss.href = dir === "rtl"
        ? bsCss.href.replace("bootstrap.min.css", "bootstrap.rtl.min.css")
        : bsCss.href.replace("bootstrap.rtl.min.css", "bootstrap.min.css");
    }
    document.querySelectorAll("[data-dir-label]").forEach(function (el) {
      el.textContent = dir === "rtl" ? "English (LTR)" : "العربية (RTL)";
    });
  }

  function toggleDir() {
    var current = root.getAttribute("dir") === "rtl" ? "rtl" : "ltr";
    var next = current === "rtl" ? "ltr" : "rtl";
    applyDir(next);
    safeSet(STORAGE_DIR, next);
  }

  function safeGet(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function safeSet(key, val) {
    try { window.localStorage.setItem(key, val); } catch (e) { /* noop */ }
  }

  /* Apply as early as possible to avoid flash */
  applyTheme(getPreferredTheme());
  var storedDir = safeGet(STORAGE_DIR);
  if (storedDir === "rtl") applyDir("rtl");

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", toggleTheme);
    });
    document.querySelectorAll("[data-dir-toggle]").forEach(function (btn) {
      btn.addEventListener("click", toggleDir);
    });
    applyTheme(root.getAttribute("data-bs-theme") || "light");
    applyDir(root.getAttribute("dir") || "ltr");

    initNavbarScroll();
    initRevealOnScroll();
    initBackToTop();
    initDashSidebar();
    initBlogFilter();
    initCountdown();
    initPasswordToggles();
    initRatingWidgets();
    initFormValidation();
    initNewsletterForms();
    initToastButtons();
    initCopyLinkButtons();
    initCounters();
    initPricingToggle();
    initQuestionPalette();
  });

  /* ---------------------------------------------------------------------
   * Navbar shadow-on-scroll
   * ------------------------------------------------------------------- */
  function initNavbarScroll() {
    var nav = document.querySelector(".navbar-ap");
    if (!nav) return;
    function onScroll() {
      if (window.scrollY > 24) nav.classList.add("is-scrolled");
      else nav.classList.remove("is-scrolled");
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------------------------------------------------------------------
   * Scroll reveal (IntersectionObserver, no deps)
   * ------------------------------------------------------------------- */
  function initRevealOnScroll() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length) return;
    if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      // No animation support (or the user asked for reduced motion) — leave elements
      // in their default, always-visible state; never arm the hidden starting state.
      return;
    }
    root.classList.add("reveal-armed");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
    // Safety net: guarantee every section becomes visible even if an observer
    // never fires for it (e.g. a screen reader jump, a bot that doesn't scroll,
    // or an unusual viewport), so content is never permanently hidden.
    setTimeout(function () {
      items.forEach(function (el) { el.classList.add("in-view"); });
    }, 4000);
  }

  /* ---------------------------------------------------------------------
   * Back to top
   * ------------------------------------------------------------------- */
  function initBackToTop() {
    var btn = document.querySelector(".back-to-top");
    if (!btn) return;
    window.addEventListener("scroll", function () {
      if (window.scrollY > 480) btn.classList.add("show");
      else btn.classList.remove("show");
    }, { passive: true });
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------------------------------------------------------------------
   * Dashboard mobile sidebar
   * ------------------------------------------------------------------- */
  function initDashSidebar() {
    var toggle = document.querySelector("[data-sidebar-toggle]");
    var sidebar = document.querySelector(".dash-sidebar");
    var backdrop = document.querySelector(".dash-backdrop");
    if (!toggle || !sidebar) return;
    function close() {
      sidebar.classList.remove("show");
      if (backdrop) backdrop.classList.remove("show");
    }
    toggle.addEventListener("click", function () {
      sidebar.classList.toggle("show");
      if (backdrop) backdrop.classList.toggle("show");
    });
    if (backdrop) backdrop.addEventListener("click", close);
  }

  /* ---------------------------------------------------------------------
   * Blog filter + search (client-side, data-category / data-title attrs)
   * ------------------------------------------------------------------- */
  function initBlogFilter() {
    var grid = document.querySelector("[data-blog-grid]");
    if (!grid) return;
    var cards = grid.querySelectorAll("[data-category]");
    var filterBtns = document.querySelectorAll("[data-filter]");
    var searchInput = document.querySelector("[data-blog-search]");
    var emptyState = document.querySelector("[data-blog-empty]");
    var activeFilter = "all";

    function applyFilters() {
      var term = (searchInput && searchInput.value || "").toLowerCase().trim();
      var visibleCount = 0;
      cards.forEach(function (card) {
        var matchesCategory = activeFilter === "all" || card.getAttribute("data-category") === activeFilter;
        var title = (card.getAttribute("data-title") || "").toLowerCase();
        var matchesSearch = term === "" || title.indexOf(term) !== -1;
        var show = matchesCategory && matchesSearch;
        card.style.display = show ? "" : "none";
        if (show) visibleCount++;
      });
      if (emptyState) emptyState.style.display = visibleCount === 0 ? "block" : "none";
    }

    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        activeFilter = btn.getAttribute("data-filter");
        applyFilters();
      });
    });
    if (searchInput) searchInput.addEventListener("input", applyFilters);
  }

  /* ---------------------------------------------------------------------
   * Coming soon countdown
   * ------------------------------------------------------------------- */
  function initCountdown() {
    var el = document.querySelector("[data-countdown]");
    if (!el) return;
    var target = new Date();
    target.setDate(target.getDate() + 21);
    var d = el.querySelector("[data-cd-days]"),
        h = el.querySelector("[data-cd-hours]"),
        m = el.querySelector("[data-cd-mins]"),
        s = el.querySelector("[data-cd-secs]");
    function tick() {
      var diff = Math.max(0, target - new Date());
      var days = Math.floor(diff / 86400000);
      var hours = Math.floor((diff % 86400000) / 3600000);
      var mins = Math.floor((diff % 3600000) / 60000);
      var secs = Math.floor((diff % 60000) / 1000);
      if (d) d.textContent = String(days).padStart(2, "0");
      if (h) h.textContent = String(hours).padStart(2, "0");
      if (m) m.textContent = String(mins).padStart(2, "0");
      if (s) s.textContent = String(secs).padStart(2, "0");
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ---------------------------------------------------------------------
   * Password show/hide toggles
   * ------------------------------------------------------------------- */
  function initPasswordToggles() {
    document.querySelectorAll("[data-toggle-password]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var input = document.querySelector(btn.getAttribute("data-toggle-password"));
        if (!input) return;
        var isPassword = input.getAttribute("type") === "password";
        input.setAttribute("type", isPassword ? "text" : "password");
        var icon = btn.querySelector("i");
        if (icon) icon.className = isPassword ? "bi bi-eye-slash" : "bi bi-eye";
      });
    });
  }

  /* ---------------------------------------------------------------------
   * Simple star rating display helper (for testimonial widgets, if data-driven)
   * ------------------------------------------------------------------- */
  function initRatingWidgets() {
    document.querySelectorAll("[data-rating]").forEach(function (el) {
      var value = parseFloat(el.getAttribute("data-rating")) || 5;
      var full = Math.floor(value);
      var html = "";
      for (var i = 0; i < 5; i++) {
        html += i < full ? '<i class="bi bi-star-fill"></i>' : '<i class="bi bi-star"></i>';
      }
      el.innerHTML = html;
    });
  }

  /* ---------------------------------------------------------------------
   * Bootstrap-style client-side validation UX
   * ------------------------------------------------------------------- */
  function initFormValidation() {
    var forms = document.querySelectorAll(".needs-validation");
    forms.forEach(function (form) {
      form.addEventListener("submit", function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
          form.classList.add("was-validated");
        } else if (form.hasAttribute("data-demo-submit")) {
          // Demo template: prevent actual navigation, show a lightweight toast.
          // Forms that represent a one-off submission (contact, comments…) are
          // then cleared so they're ready for a fresh entry; forms that edit
          // standing account data (data-keep-values, e.g. Profile) keep their
          // values in place instead of wiping them.
          event.preventDefault();
          showToast(form.getAttribute("data-demo-submit") || "Submitted successfully.");
          if (!form.hasAttribute("data-keep-values")) {
            form.reset();
          }
          form.classList.remove("was-validated");
        } else {
          form.classList.add("was-validated");
        }
      });
    });
  }

  /* ---------------------------------------------------------------------
   * Footer newsletter form — demo-only "subscribe" confirmation
   * ------------------------------------------------------------------- */
  function initCopyLinkButtons() {
    document.querySelectorAll("[data-copy-link]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var url = window.location.href;
        var done = function () { showToast("Link copied to clipboard."); };
        var fail = function () { showToast("Couldn't copy the link — copy it from the address bar."); };
        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(url).then(done, fail);
        } else {
          var tmp = document.createElement("textarea");
          tmp.value = url;
          tmp.style.position = "fixed";
          tmp.style.opacity = "0";
          document.body.appendChild(tmp);
          tmp.select();
          try {
            document.execCommand("copy");
            done();
          } catch (e) {
            fail();
          }
          document.body.removeChild(tmp);
        }
      });
    });
  }

  function initNewsletterForms() {
    document.querySelectorAll("[data-newsletter-form]").forEach(function (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        var input = form.querySelector('input[type="email"]');
        if (input && !input.checkValidity()) {
          input.reportValidity();
          return;
        }
        showToast(form.getAttribute("data-success-message") || "Subscribed successfully.");
        form.reset();
      });
    });
  }

  /* ---------------------------------------------------------------------
   * Generic "demo action" buttons — show a confirmation toast on click
   * (e.g. Profile page's "Change Photo" button).
   * ------------------------------------------------------------------- */
  function initToastButtons() {
    document.querySelectorAll("[data-toast-btn]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        showToast(btn.getAttribute("data-toast-btn") || "Done.");
      });
    });
  }

  function showToast(message) {
    var wrap = document.querySelector(".toast-container");
    if (!wrap) {
      wrap = document.createElement("div");
      wrap.className = "toast-container position-fixed bottom-0 end-0 p-3";
      wrap.style.zIndex = 1080;
      document.body.appendChild(wrap);
    }
    var toastEl = document.createElement("div");
    toastEl.className = "toast align-items-center text-bg-dark border-0";
    toastEl.setAttribute("role", "alert");
    toastEl.innerHTML =
      '<div class="d-flex"><div class="toast-body"><i class="bi bi-check-circle-fill text-success me-2"></i>' +
      message + '</div><button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button></div>';
    wrap.appendChild(toastEl);
    if (window.bootstrap) {
      var t = new window.bootstrap.Toast(toastEl, { delay: 3500 });
      t.show();
      toastEl.addEventListener("hidden.bs.toast", function () { toastEl.remove(); });
    }
  }
  window.APShowToast = showToast;

  /* ---------------------------------------------------------------------
   * Animated counters (stat strips)
   * ------------------------------------------------------------------- */
  function initCounters() {
    var counters = document.querySelectorAll("[data-counter]");
    if (!counters.length) return;
    var animate = function (el) {
      var target = parseFloat(el.getAttribute("data-counter"));
      var suffix = el.getAttribute("data-suffix") || "";
      var duration = 1400;
      var start = null;
      function step(ts) {
        if (!start) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var value = Math.floor(progress * target);
        el.textContent = value.toLocaleString() + suffix;
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target.toLocaleString() + suffix;
      }
      requestAnimationFrame(step);
    };
    if (!("IntersectionObserver" in window)) {
      counters.forEach(animate);
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animate(entry.target);
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { io.observe(el); });
  }

  /* ---------------------------------------------------------------------
   * Monthly / Yearly pricing toggle
   * ------------------------------------------------------------------- */
  function initPricingToggle() {
    var toggle = document.querySelector("[data-pricing-toggle]");
    if (!toggle) return;
    var monthlyBtn = toggle.querySelector('[data-period="monthly"]');
    var yearlyBtn = toggle.querySelector('[data-period="yearly"]');
    var monthlyEls = document.querySelectorAll("[data-price-monthly]");
    var yearlyEls = document.querySelectorAll("[data-price-yearly]");
    function setPeriod(period) {
      monthlyBtn.classList.toggle("btn-gradient", period === "monthly");
      monthlyBtn.classList.toggle("btn-light", period !== "monthly");
      yearlyBtn.classList.toggle("btn-gradient", period === "yearly");
      yearlyBtn.classList.toggle("btn-light", period !== "yearly");
      monthlyEls.forEach(function (el) { el.style.display = period === "monthly" ? "" : "none"; });
      yearlyEls.forEach(function (el) { el.style.display = period === "yearly" ? "" : "none"; });
    }
    if (monthlyBtn) monthlyBtn.addEventListener("click", function () { setPeriod("monthly"); });
    if (yearlyBtn) yearlyBtn.addEventListener("click", function () { setPeriod("yearly"); });
  }

  /* ---------------------------------------------------------------------
   * Mock test question palette (student test-attempt page demo interaction)
   * ------------------------------------------------------------------- */
  function initQuestionPalette() {
    var palette = document.querySelector("[data-q-palette]");
    if (!palette) return;
    var buttons = palette.querySelectorAll(".q-palette-btn");
    var qTitle = document.querySelector("[data-q-title]");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (b) { b.classList.remove("current"); });
        btn.classList.add("current");
        if (qTitle) qTitle.textContent = "Question " + btn.textContent.trim();
      });
    });
    document.querySelectorAll("[data-option-row]").forEach(function (row) {
      row.addEventListener("click", function () {
        var group = row.closest("[data-options-group]");
        if (group) group.querySelectorAll("[data-option-row]").forEach(function (r) { r.classList.remove("selected"); });
        row.classList.add("selected");
        var current = palette.querySelector(".q-palette-btn.current");
        if (current) { current.classList.remove("not-answered"); current.classList.add("answered"); }
      });
    });
    var markBtn = document.querySelector("[data-mark-review]");
    if (markBtn) {
      markBtn.addEventListener("click", function () {
        var current = palette.querySelector(".q-palette-btn.current");
        if (current) current.classList.add("marked");
      });
    }
  }
})();
