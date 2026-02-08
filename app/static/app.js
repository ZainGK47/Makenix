const form = document.getElementById("plan-form");
const results = document.getElementById("plan-results");

const renderSteps = (steps) => {
  if (!steps.length) {
    results.innerHTML = '<p class="muted">Tell us your goal to generate a plan.</p>';
    return;
  }

  results.innerHTML = steps
    .map(
      (step) => `
      <div class="result">
        <strong>${step.title}</strong>
        <p class="muted">${step.detail}</p>
      </div>
    `
    )
    .join("");
};

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const goal = formData.get("goal");

  results.innerHTML = '<p class="muted">Generating your plan...</p>';

  const response = await fetch("/api/plan", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ goal }),
  });
  const payload = await response.json();
  renderSteps(payload.steps || []);
});
