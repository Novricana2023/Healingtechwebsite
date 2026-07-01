(function () {
    document.querySelectorAll('.faq-item .faq-q').forEach(function (q) {
        q.addEventListener('click', function () {
            var item = this.parentElement;
            var wasOpen = item.classList.contains('open');
            document.querySelectorAll('.faq-item').forEach(function (i) { i.classList.remove('open'); });
            if (!wasOpen) item.classList.add('open');
        });
    });
})();
