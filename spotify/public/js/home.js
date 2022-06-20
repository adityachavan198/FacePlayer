var audio = " ";
for (var i = 1; i < 15; i++) {
  audio = "myAudio" + i
var audio = document.getElementById(audio);

}

function togglePlay(pos){
  for (var i = 1; i < 15; i++) {
    if (i==pos) {
      audio = "myAudio" + i
      continue
    }
    else {
      audio = "myAudio" + i
      audio = document.getElementById(audio)
      audio.pause()
      console.log(pos);
    }
  }
  audio = "myAudio" + pos
    audio = document.getElementById(audio)
    console.log(audio + "123");

  return audio.paused ? audio.play() : audio.pause();
}


// function togglePlay1() {
//   myAudio1.pause()
//   myAudio2.pause()
//   myAudio3.pause()
//   return myAudio1.paused ? myAudio1.play() : myAudio1.pause();
// };
// function togglePlay2() {
//   myAudio1.pause()
//   myAudio3.pause()
//   return myAudio2.paused ? myAudio2.play() : myAudio2.pause();
// };
// function togglePlay3() {
//   myAudio1.pause()
//   myAudio2.pause()
//   return myAudio3.paused ? myAudio3.play() : myAudio3.pause();
// };
