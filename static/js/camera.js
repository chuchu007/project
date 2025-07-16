const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const snapshot = document.getElementById("snapshot");
const captureBtn = document.getElementById("capture");

navigator.mediaDevices.getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
  })
  .catch((err) => {
    console.error("Error accessing webcam: ", err);
  });

captureBtn.addEventListener("click", () => {
  const context = canvas.getContext("2d");
  canvas.style.display = "block";
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  const dataURL = canvas.toDataURL("image/png");
  snapshot.src = dataURL;
});
