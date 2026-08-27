/*!
 * LS Academy — Chart.js initializers
 * Loaded only on pages that need charts (admin analytics, student performance).
 * Reads CSS custom properties so charts follow the active theme automatically.
 */
(function () {
  "use strict";

  function cssVar(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  }

  function themeColors() {
    return {
      primary: cssVar("--ap-primary") || "#4338ca",
      accent: cssVar("--ap-accent") || "#f59e0b",
      success: cssVar("--ap-success") || "#16a34a",
      danger: cssVar("--ap-danger") || "#e11d48",
      info: cssVar("--ap-info") || "#0891b2",
      text: cssVar("--ap-text") || "#1c1d2e",
      muted: cssVar("--ap-text-muted") || "#6b6d85",
      border: cssVar("--ap-border") || "#e7e8f2",
      surface: cssVar("--ap-surface") || "#ffffff"
    };
  }

  function baseOptions(c) {
    Chart.defaults.font.family = "Manrope, sans-serif";
    Chart.defaults.color = c.muted;
    Chart.defaults.borderColor = c.border;
  }

  function initAll() {
    if (typeof Chart === "undefined") return;
    var c = themeColors();
    baseOptions(c);

    /* Admin: Revenue / Enrollment trend (line) */
    var revEl = document.getElementById("chartRevenueTrend");
    if (revEl) {
      new Chart(revEl, {
        type: "line",
        data: {
          labels: ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb"],
          datasets: [
            {
              label: "Revenue (₹k)",
              data: [180, 210, 195, 260, 300, 285, 340, 365, 330, 390, 420, 455],
              borderColor: c.primary,
              backgroundColor: hexToRgba(c.primary, 0.12),
              fill: true,
              tension: 0.4,
              pointRadius: 0,
              borderWidth: 3
            },
            {
              label: "New enrollments",
              data: [40, 55, 48, 60, 70, 66, 78, 84, 76, 90, 96, 104],
              borderColor: c.accent,
              backgroundColor: "transparent",
              borderDash: [5, 4],
              tension: 0.4,
              pointRadius: 0,
              borderWidth: 2,
              yAxisID: "y1"
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          interaction: { mode: "index", intersect: false },
          plugins: { legend: { position: "top", labels: { usePointStyle: true, boxWidth: 8 } } },
          scales: {
            y: { grid: { color: c.border }, ticks: { callback: function (v) { return "₹" + v + "k"; } } },
            y1: { position: "right", grid: { display: false }, ticks: { display: false } },
            x: { grid: { display: false } }
          }
        }
      });
    }

    /* Admin: Students by exam category (doughnut) */
    var catEl = document.getElementById("chartExamCategories");
    if (catEl) {
      new Chart(catEl, {
        type: "doughnut",
        data: {
          labels: ["Banking", "SSC", "Civil Services", "Engineering (JEE)", "Medical (NEET)"],
          datasets: [{
            data: [420, 380, 260, 310, 275],
            backgroundColor: [c.primary, c.accent, c.info, c.success, c.danger],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: "68%",
          plugins: { legend: { position: "bottom", labels: { usePointStyle: true, boxWidth: 8, padding: 14 } } }
        }
      });
    }

    /* Admin: Weekly active students (bar) */
    var activeEl = document.getElementById("chartWeeklyActive");
    if (activeEl) {
      new Chart(activeEl, {
        type: "bar",
        data: {
          labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          datasets: [{
            label: "Active students",
            data: [820, 932, 901, 934, 1090, 1230, 980],
            backgroundColor: hexToRgba(c.primary, 0.75),
            borderRadius: 8,
            maxBarThickness: 28
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: { y: { grid: { color: c.border } }, x: { grid: { display: false } } }
        }
      });
    }

    /* Student: Topic-wise performance (radar) */
    var radarEl = document.getElementById("chartTopicRadar");
    if (radarEl) {
      new Chart(radarEl, {
        type: "radar",
        data: {
          labels: ["Quant Aptitude", "Reasoning", "English", "General Awareness", "Computer Aptitude", "Current Affairs"],
          datasets: [{
            label: "Your accuracy %",
            data: [72, 65, 80, 58, 74, 62],
            borderColor: c.primary,
            backgroundColor: hexToRgba(c.primary, 0.18),
            pointBackgroundColor: c.primary
          }, {
            label: "Topper average %",
            data: [85, 82, 88, 78, 86, 80],
            borderColor: c.accent,
            backgroundColor: hexToRgba(c.accent, 0.08),
            pointBackgroundColor: c.accent
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: "bottom", labels: { usePointStyle: true, boxWidth: 8 } } },
          scales: {
            r: {
              angleLines: { color: c.border },
              grid: { color: c.border },
              pointLabels: { color: c.text, font: { size: 11 } },
              ticks: { display: false, backdropColor: "transparent" },
              suggestedMin: 0, suggestedMax: 100
            }
          }
        }
      });
    }

    /* Student: Score trend over attempts (line) */
    var scoreTrendEl = document.getElementById("chartScoreTrend");
    if (scoreTrendEl) {
      new Chart(scoreTrendEl, {
        type: "line",
        data: {
          labels: ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5", "Test 6", "Test 7", "Test 8"],
          datasets: [{
            label: "Your score %",
            data: [54, 58, 61, 59, 66, 70, 68, 74],
            borderColor: c.primary,
            backgroundColor: hexToRgba(c.primary, 0.15),
            fill: true,
            tension: 0.35,
            pointRadius: 3,
            pointBackgroundColor: c.primary
          }, {
            label: "Class average %",
            data: [50, 51, 53, 54, 55, 57, 58, 60],
            borderColor: c.muted,
            borderDash: [4, 4],
            fill: false,
            tension: 0.35,
            pointRadius: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: "top", labels: { usePointStyle: true, boxWidth: 8 } } },
          scales: { y: { min: 0, max: 100, grid: { color: c.border } }, x: { grid: { display: false } } }
        }
      });
    }

    /* Student: correct vs incorrect breakdown (doughnut) */
    var breakdownEl = document.getElementById("chartScoreBreakdown");
    if (breakdownEl) {
      var bdCorrect = parseInt(breakdownEl.getAttribute("data-correct"), 10);
      var bdIncorrect = parseInt(breakdownEl.getAttribute("data-incorrect"), 10);
      var bdSkipped = parseInt(breakdownEl.getAttribute("data-skipped"), 10);
      var bdData = (!isNaN(bdCorrect) && !isNaN(bdIncorrect) && !isNaN(bdSkipped))
        ? [bdCorrect, bdIncorrect, bdSkipped] : [68, 22, 10];
      new Chart(breakdownEl, {
        type: "doughnut",
        data: {
          labels: ["Correct", "Incorrect", "Unattempted"],
          datasets: [{
            data: bdData,
            backgroundColor: [c.success, c.danger, c.border],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: "72%",
          plugins: { legend: { position: "bottom", labels: { usePointStyle: true, boxWidth: 8 } } }
        }
      });
    }

    /* Student: subject-wise accuracy (horizontal bar) */
    var subjEl = document.getElementById("chartSubjectAccuracy");
    if (subjEl) {
      new Chart(subjEl, {
        type: "bar",
        data: {
          labels: ["Quant Aptitude", "Reasoning", "English Language", "General Awareness", "Computer Aptitude"],
          datasets: [{
            label: "Accuracy %",
            data: [72, 65, 80, 58, 74],
            backgroundColor: [c.primary, c.accent, c.success, c.danger, c.info],
            borderRadius: 8
          }]
        },
        options: {
          indexAxis: "y",
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: { x: { max: 100, grid: { color: c.border } }, y: { grid: { display: false } } }
        }
      });
    }
  }

  function hexToRgba(hex, alpha) {
    if (!hex) return "rgba(67,56,202," + alpha + ")";
    hex = hex.replace("#", "");
    if (hex.length === 3) hex = hex.split("").map(function (h) { return h + h; }).join("");
    var r = parseInt(hex.substring(0, 2), 16);
    var g = parseInt(hex.substring(2, 4), 16);
    var b = parseInt(hex.substring(4, 6), 16);
    if (isNaN(r) || isNaN(g) || isNaN(b)) return "rgba(67,56,202," + alpha + ")";
    return "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
  }

  document.addEventListener("DOMContentLoaded", initAll);

  /* Re-render charts on theme toggle so colors stay in sync */
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        setTimeout(function () {
          document.querySelectorAll("canvas").forEach(function (canvas) {
            var chart = Chart.getChart(canvas);
            if (chart) chart.destroy();
          });
          initAll();
        }, 60);
      });
    });
  });
})();
