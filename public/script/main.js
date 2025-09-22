// helper to call the exposed Python API
async function callPy(method, ...args) {
  if (window.pywebview) {
    try {
      const res = await window.pywebview.api[method](...args);
      return res;
    } catch (e) {
      console.error("pywebview API error:", e);
    }
  }
}

// minimize button
document.getElementById("min").addEventListener("click", async () => {
  await callPy("minimize");
});

// close button
document.getElementById("close").addEventListener("click", async () => {
  await callPy("close");
});
