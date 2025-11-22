function pad(n){return String(n).padStart(2,'0')}
function updateClock(){
  const now=new Date()
  let h=now.getHours()
  const m=pad(now.getMinutes())
  const s=pad(now.getSeconds())
  const ampm=h>=12?'PM':'AM'
  h=h%12||12
  document.getElementById('time').textContent=`${pad(h)}:${m}:${s} ${ampm}`
  document.getElementById('date').textContent=now.toLocaleDateString(undefined,{weekday:'long',year:'numeric',month:'short',day:'numeric'})
}
updateClock()
setInterval(updateClock,1000)
