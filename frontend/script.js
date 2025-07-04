async function getHello() {
  const res = await fetch("/api/hello");
  const data = await res.json();
  document.getElementById("response").innerText = data.message;
}