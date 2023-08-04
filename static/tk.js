// script.js (add this to a separate JavaScript file)

let currentIndex = 0;
const posts = document.querySelectorAll('.post');

function scrollToNextPost() {
  currentIndex = (currentIndex + 1) % posts.length;
  posts[currentIndex].scrollIntoView({ behavior: 'smooth' });
}

document.addEventListener('wheel', (e) => {
  e.preventDefault();
  scrollToNextPost();
});
