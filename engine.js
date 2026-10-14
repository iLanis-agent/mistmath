(function (root) {
  "use strict";
  var ML_PER_M3 = 30; // labeled daily output per cubic meter of dry winter room, mL

  function round1(x) { return Math.round(x * 10) / 10; }

  function mistPlan(areaM2, ceilingM) {
    if (!(areaM2 > 0) || !(ceilingM > 0)) return { error: "the room and the ceiling must be positive" };
    var ml = Math.round(areaM2 * ceilingM * ML_PER_M3);
    var verdict;
    if (ml <= 1500) verdict = "a tabletop unit";
    else if (ml <= 4000) verdict = "a console job";
    else verdict = "a whole-house conversation";
    return { ml: ml, verdict: verdict };
  }

  function tankPlan(mlPerDay, tankL) {
    if (!(mlPerDay > 0) || !(tankL > 0)) return { error: "the mist and the tank must be positive" };
    var days = round1(tankL * 1000 / mlPerDay);
    var verdict;
    if (days >= 2) verdict = "an every-other-day job";
    else if (days >= 1) verdict = "a daily top-up";
    else verdict = "a twice-a-day chore";
    return { days: days, verdict: verdict };
  }

  function wickPlan(hoursPerDay, wickLifeH) {
    if (!(hoursPerDay > 0) || !(wickLifeH > 0)) return { error: "the hours and the wick must be positive" };
    var days = Math.floor(wickLifeH / hoursPerDay);
    var verdict;
    if (days >= 90) verdict = "a full season";
    else if (days >= 45) verdict = "half a season";
    else verdict = "a monthly consumable";
    return { days: days, verdict: verdict };
  }

  function renderMist(r, areaM2, ceilingM) {
    return "Your " + areaM2 + " m2 room with a " + ceilingM + " m ceiling asks for " + r.ml
      + " mL a day - " + r.verdict + ".";
  }

  function renderTank(r, mlPerDay, tankL) {
    var every = r.days === 1 ? "every day" : "every " + r.days + " days";
    return mlPerDay + " mL a day from a " + tankL + " L tank is a refill " + every
      + " - " + r.verdict + ".";
  }

  function renderWick(r, hoursPerDay, wickLifeH) {
    return "A labeled " + wickLifeH + " h wick at " + hoursPerDay + " h a day lasts " + r.days
      + " days - " + r.verdict + ".";
  }

  var api = { mistPlan: mistPlan, tankPlan: tankPlan, wickPlan: wickPlan, renderMist: renderMist, renderTank: renderTank, renderWick: renderWick };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.MistMath = api;
})(this);
