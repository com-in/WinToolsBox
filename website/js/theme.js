function toggleTheme() {
    const link = document.getElementById('theme-style');
    if (link.getAttribute('href') === 'css/themes/default.css') {
        link.setAttribute('href', 'css/themes/dark.css');
    } else {
        link.setAttribute('href', 'css/themes/default.css');
    }
}