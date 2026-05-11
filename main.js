import './style.css'
import Lenis from '@studio-freight/lenis'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

// Initialize Lenis Smooth Scroll
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
  infinite: false,
})

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}
requestAnimationFrame(raf)

// Connect GSAP to Lenis
lenis.on('scroll', ScrollTrigger.update)

gsap.ticker.add((time)=>{
  lenis.raf(time * 1000)
})
gsap.ticker.lagSmoothing(0)

// Preloader Animation
window.addEventListener('load', () => {
  const tl = gsap.timeline();

  const counterObj = { value: 0 };
  const counterEl = document.querySelector('.preloader-counter');

  if (counterEl) {
    tl.to(counterObj, {
      value: 100,
      duration: 1.5,
      ease: 'power3.inOut',
      onUpdate: () => {
        counterEl.innerHTML = Math.round(counterObj.value) + '%';
      }
    }, 0)
    .to(counterEl, {
      opacity: 1,
      duration: 0.5
    }, 0);
  }

  tl.to('.preloader-text', {
    opacity: 1,
    duration: 1.5,
    ease: 'power3.inOut'
  }, 0)
  .to('.preloader', {
    yPercent: -100,
    duration: 1.2,
    ease: 'power4.inOut',
    delay: 0.2
  })
  
  // New Hero Animations
  const heroNew = document.querySelector('.hero-new');
  if(heroNew) {
    // Initial state
    gsap.set('.hero-image-wrapper', {
      y: 100,
      opacity: 0
    });
    gsap.set('.hero-image-wrapper img', {
      scale: 1.1
    });

    tl.fromTo('.hero-title', {
      opacity: 0,
      y: 30
    }, {
      opacity: 1,
      y: 0,
      duration: 1.5,
      ease: 'power3.out'
    }, '-=0.5')
    .fromTo('.hero-buttons .btn', {
      opacity: 0,
      y: 20
    }, {
      opacity: 1,
      y: 0,
      stagger: 0.2,
      duration: 1,
      ease: 'power3.out'
    }, '-=1.2')
    .to('.hero-image-wrapper', {
      y: 0,
      opacity: 1,
      duration: 1.5,
      ease: 'power3.out'
    }, '-=1.5')
    .to('.hero-image-wrapper img', {
      scale: 1,
      duration: 2,
      ease: 'power2.out'
    }, '-=1.5');
  }
});

// Scroll Animations

// Reveal Text
const revealTextElements = document.querySelectorAll('.reveal-text');
revealTextElements.forEach((el) => {
  gsap.fromTo(el, 
    { opacity: 0, y: 50 },
    {
      opacity: 1, 
      y: 0,
      duration: 1,
      ease: 'power3.out',
      scrollTrigger: {
        trigger: el,
        start: 'top 80%',
      }
    }
  );
});

// Reveal Fade
const revealFadeElements = document.querySelectorAll('.reveal-fade');
revealFadeElements.forEach((el) => {
  gsap.fromTo(el, 
    { opacity: 0, y: 30 },
    {
      opacity: 1, 
      y: 0,
      duration: 1,
      ease: 'power3.out',
      stagger: 0.2,
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',
      }
    }
  );
});

// Reveal Image with slight scale
// Reveal Image with clip-path
const revealImageElements = document.querySelectorAll('.reveal-image');
revealImageElements.forEach((el) => {
  gsap.fromTo(el, 
    { clipPath: 'inset(10% 10% 10% 10% round 20px)', scale: 1.1, opacity: 0 },
    {
      clipPath: 'inset(0% 0% 0% 0% round 20px)',
      scale: 1,
      opacity: 1,
      duration: 1.5,
      ease: 'expo.out',
      scrollTrigger: {
        trigger: el,
        start: 'top 80%',
      }
    }
  );
});

// Staggered Grids (Services, Portfolio, Awards, Contact Links)
const staggerGrids = document.querySelectorAll('.services-grid, .portfolio-grid, .awards-grid, .links-grid');
staggerGrids.forEach((grid) => {
  const items = grid.children;
  gsap.fromTo(items,
    { opacity: 0, y: 40 },
    {
      opacity: 1,
      y: 0,
      duration: 1,
      stagger: 0.15,
      ease: 'power3.out',
      scrollTrigger: {
        trigger: grid,
        start: 'top 85%',
      }
    }
  );
});

// Parallax Effects
const parallaxImages = document.querySelectorAll('[data-scroll-speed]');
parallaxImages.forEach((el) => {
  const speed = el.getAttribute('data-scroll-speed');
  
  gsap.to(el, {
    y: () => `${speed * 100}px`,
    ease: 'none',
    scrollTrigger: {
      trigger: el.parentElement,
      start: 'top bottom',
      end: 'bottom top',
      scrub: true,
    }
  });
});

// Navbar background on scroll
ScrollTrigger.create({
  start: 'top -100',
  end: 99999,
  toggleClass: {className: 'scrolled', targets: '.navbar'}
});

// Custom Cursor Logic
const customCursor = document.querySelector('.custom-cursor');
if(customCursor) {
  // Set initial position out of view
  gsap.set(customCursor, { x: -100, y: -100 });
  
  // Move cursor with GSAP for smooth easing
  document.addEventListener('mousemove', (e) => {
    gsap.to(customCursor, {
      x: e.clientX - 18, // Half of 36px width
      y: e.clientY - 18, // Half of 36px height
      duration: 0.15,
      ease: 'power2.out'
    });
  });

  // Add hover effects on clickable elements
  const hoverTargets = document.querySelectorAll('a, button, .btn, .grid-item, .service-card');
  hoverTargets.forEach(target => {
    target.addEventListener('mouseenter', () => customCursor.classList.add('hover'));
    target.addEventListener('mouseleave', () => customCursor.classList.remove('hover'));
  });
}

// Mobile Hamburger Menu
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    
    // Optional: Animate hamburger lines
    const spans = hamburger.querySelectorAll('span');
    if (navLinks.classList.contains('active')) {
      spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
      spans[0].style.transform = 'none';
      spans[1].style.opacity = '1';
      spans[2].style.transform = 'none';
    }
  });

  // Close menu when clicking a link
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
      const spans = hamburger.querySelectorAll('span');
      spans[0].style.transform = 'none';
      spans[1].style.opacity = '1';
      spans[2].style.transform = 'none';
    });
  });
}


// Venue Booking Modal Logic
document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.venue-card-modern');
  const modal = document.getElementById('bookingModal');
  if(!modal) return;
  
  const venueInput = document.getElementById('venueInput');
  const closeBtn = document.getElementById('closeModalBtn');
  const bookForm = document.getElementById('bookingForm');
  
  cards.forEach(card => {
    card.addEventListener('click', (e) => {
      // Don't trigger if they clicked a link inside the card
      if(e.target.tagName.toLowerCase() === 'a') return;
      
      const venueName = card.querySelector('h4').innerText;
      venueInput.value = venueName;
      modal.style.display = 'flex';
      // Animate modal in
      gsap.fromTo('.modal-content', {y: 50, opacity: 0}, {y: 0, opacity: 1, duration: 0.4, ease: 'power2.out'});
    });
  });
  
  closeBtn.addEventListener('click', () => {
    gsap.to('.modal-content', {y: 50, opacity: 0, duration: 0.3, ease: 'power2.in', onComplete: () => {
      modal.style.display = 'none';
    }});
  });
  
  window.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeBtn.click();
    }
  });
  
  bookForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const nama = document.getElementById('bookingName').value;
    const date = document.getElementById('bookingDate').value;
    const venue = venueInput.value;
    const notes = document.getElementById('bookingNotes').value;
    
    let text = `Halo Admin Oretta, saya tertarik memesan Intimate Package 24Jt All-In.\n\n*Nama:* ${nama}\n*Tanggal Pernikahan:* ${date}\n*Venue Pilihan:* ${venue}\n*Catatan:* ${notes}\n\nMohon informasi ketersediaan dan detail lebih lanjut.`;
    const waUrl = `https://wa.me/6285973929029?text=${encodeURIComponent(text)}`;
    window.open(waUrl, '_blank');
    closeBtn.click();
  });
});

// FAQ Accordion Logic
document.addEventListener('DOMContentLoaded', () => {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    const icon = item.querySelector('.faq-icon');
    
    if (question && answer && icon) {
      question.addEventListener('click', () => {
        const isOpen = answer.style.maxHeight && answer.style.maxHeight !== '0px';
        
        // Close all other FAQs
        document.querySelectorAll('.faq-answer').forEach(a => {
          a.style.maxHeight = '0px';
          a.style.paddingBottom = '0';
        });
        document.querySelectorAll('.faq-icon').forEach(i => {
          i.style.transform = 'rotate(0deg)';
        });
        
        if (!isOpen) {
          answer.style.maxHeight = answer.scrollHeight + 30 + 'px';
          answer.style.paddingBottom = '1.5rem';
          icon.style.transform = 'rotate(45deg)';
        }
      });
    }
  });
});
