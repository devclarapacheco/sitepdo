function showPage(page) {
    var pages = document.querySelectorAll('div[id^=home], div[id^=ranking], div[id^=grupos]');
    pages.forEach(pageElement => {
        pageElement.style.display = 'none';
    });

    document.getElementById(page).style.display = 'block';

    var links = document.querySelectorAll('.menu-links a');
    links.forEach(link => {
        link.classList.remove('active');
    });

    document.querySelector('.menu-links a[href="#"][onclick="showPage(\'' + page + '\')"]').classList.add('active');
    
    // Exibindo o rodapé se for a página inicial
    if (page === 'home') {
        var footer = document.querySelector('.footer');
        footer.style.display = 'block';
    } else {
        var footer = document.querySelector('.footer');
        footer.style.display = 'none';
    }
}

var rows = document.querySelectorAll('table tr');
rows.forEach(row => {
    row.addEventListener('mouseover', function() {
        this.classList.add('highlight');
    });
    row.addEventListener('mouseout', function() {
        this.classList.remove('highlight');
    });
});

// Função para controlar o acordeão
function toggleAccordion(button) {
    button.classList.toggle("active");
    var panel = button.nextElementSibling;
    if (panel.style.display === "block") {
        panel.style.display = "none";
    } else {
        panel.style.display = "block";
    }
}

function mostrarLinkWhatsapp(grupo) {
    var panels = document.querySelectorAll('.panel');
    panels.forEach(panel => {
        panel.style.display = 'none';
    });

    var whatsappSpace = document.getElementById(grupo + '-whatsapp');
    whatsappSpace.style.display = 'block';
}
/*deixa os acordeões fechados quando clica na aba grupos*/
function hidePanels() {
    var panels = document.querySelectorAll('#grupos .panel');
    panels.forEach(panel => {
        panel.style.display = 'none';
    });
}

// Chama a função para ocultar os painéis ao carregar a página
window.onload = function() {
    hidePanels();
};