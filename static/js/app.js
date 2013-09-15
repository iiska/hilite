$(document).ready(function() {
    var hash = window.location.hash;
    if (hash && hash !== '') {
        var lineno_el = $('td.linenos');
        var code_el = $('td.code');
        $('a[name="'+hash.substr(1)+'"]', code_el)
            .addClass("highlight-line")
            .width(code_el.width()+lineno_el.width());
    }
});
