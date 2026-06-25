/**
 * QuestIA - Main JS
 * Global functionalities: Mobile Menu, Smooth Scroll, etc.
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Mobile Menu (Burger)
    const burger = document.querySelector('.nav-burger');
    const navLinks = document.querySelector('.nav-links');
    
    if (burger) {
        burger.addEventListener('click', () => {
            burger.classList.toggle('is-active');
            navLinks.classList.toggle('is-visible');
            
            // UX: Prevent scroll when menu is open
            document.body.style.overflow = burger.classList.contains('is-active') ? 'hidden' : 'auto';
        });
    }

    // 2. Smooth Scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                // If mobile menu open, close it
                if (burger && burger.classList.contains('is-active')) {
                    burger.click();
                }
                
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 3. Reveal Animation on scroll (Simple)
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.mission-card, .section-head').forEach(el => {
        el.classList.add('reveal-init');
        observer.observe(el);
    });

});
