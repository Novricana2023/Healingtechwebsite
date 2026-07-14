(function () {
    'use strict';

    function animateCounter(el, target, duration) {
        var start = 0;
        var startTime = null;
        duration = duration || 1800;

        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            var progress = Math.min((timestamp - startTime) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            var value = Math.round(start + (target - start) * eased);
            el.textContent = value;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                el.textContent = target;
            }
        }

        window.requestAnimationFrame(step);
    }

    function initChallengeCounters() {
        var section = document.querySelector('.challenge-section');
        if (!section || !('IntersectionObserver' in window)) {
            section && section.querySelectorAll('[data-challenge-counter]').forEach(function (el) {
                el.textContent = el.getAttribute('data-challenge-counter');
            });
            return;
        }

        var ran = false;
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !ran) {
                    ran = true;
                    section.querySelectorAll('[data-challenge-counter]').forEach(function (el) {
                        var target = parseInt(el.getAttribute('data-challenge-counter'), 10);
                        if (!isNaN(target)) {
                            animateCounter(el, target);
                        }
                    });
                    observer.disconnect();
                }
            });
        }, { threshold: 0.15 });

        observer.observe(section);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initChallengeCounters);
    } else {
        initChallengeCounters();
    }
})();
