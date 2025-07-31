#!/usr/bin/env python3
"""
Skrypt do konwersji strony La Li Lu na PDF
Używa weasyprint do generowania wysokiej jakości PDF
"""

import os
import sys
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def convert_html_to_pdf(input_file, output_file):
    """Konwertuje plik HTML na PDF"""
    
    print(f"🔄 Konwertuję {input_file} na {output_file}...")
    
    # Konfiguracja fontów
    font_config = FontConfiguration()
    
    # Wczytanie pliku HTML
    html = HTML(filename=input_file)
    
    # Dodanie dodatkowych stylów CSS dla PDF
    pdf_css = CSS(string='''
        @page {
            size: A4;
            margin: 1cm;
            @top-center {
                content: "La Li Lu - Perfumeria Niszowa";
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: "Strona " counter(page) " z " counter(pages);
                font-size: 10pt;
                color: #666;
            }
        }
        
        body {
            font-family: 'Lato', sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Dancing Script', cursive;
            color: #e91e63;
            page-break-after: avoid;
        }
        
        .hero {
            page-break-inside: avoid;
            margin-bottom: 2em;
        }
        
        .section {
            page-break-inside: avoid;
            margin-bottom: 2em;
        }
        
        .fragrances-showcase {
            page-break-inside: avoid;
        }
        
        .newsletter {
            page-break-inside: avoid;
            background: linear-gradient(135deg, #e91e63 0%, #ad1457 100%);
            color: white;
            padding: 2em;
            border-radius: 10px;
            margin: 2em 0;
        }
        
        .footer {
            page-break-inside: avoid;
            margin-top: 2em;
            padding: 2em;
            background: #f8f9fa;
            border-top: 2px solid #e91e63;
        }
        
        img {
            max-width: 100%;
            height: auto;
            page-break-inside: avoid;
        }
        
        .container {
            max-width: none;
            margin: 0;
            padding: 0;
        }
        
        /* Ukryj elementy niepotrzebne w PDF */
        .mobile-menu-toggle,
        .scroll-to-top,
        .floating-particles {
            display: none !important;
        }
        
        /* Poprawki dla responsywności w PDF */
        .grid {
            display: block;
        }
        
        .grid > * {
            margin-bottom: 1em;
        }
        
        /* Stylizacja linków */
        a {
            color: #e91e63;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        /* Stylizacja przycisków */
        .btn {
            background: #e91e63;
            color: white;
            padding: 0.5em 1em;
            border-radius: 5px;
            display: inline-block;
            margin: 0.5em 0;
        }
        
        /* Stylizacja formularzy */
        input, textarea, select {
            border: 1px solid #ddd;
            padding: 0.5em;
            border-radius: 5px;
            margin: 0.5em 0;
        }
        
        /* Stylizacja tabel */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 0.5em;
            text-align: left;
        }
        
        th {
            background: #f8f9fa;
            font-weight: bold;
        }
    ''', font_config=font_config)
    
    try:
        # Generowanie PDF
        html.write_pdf(
            output_file,
            stylesheets=[pdf_css],
            font_config=font_config
        )
        
        print(f"✅ PDF został pomyślnie utworzony: {output_file}")
        print(f"📄 Rozmiar pliku: {os.path.getsize(output_file) / 1024:.1f} KB")
        
    except Exception as e:
        print(f"❌ Błąd podczas konwersji: {e}")
        sys.exit(1)

def main():
    """Główna funkcja"""
    
    # Pliki do konwersji
    files_to_convert = [
        ('index.html', 'La_Li_Lu_Strona_Glowna.pdf'),
        ('polityka-prywatnosci.html', 'La_Li_Lu_Polityka_Prywatnosci.pdf'),
        ('regulamin.html', 'La_Li_Lu_Regulamin.pdf')
    ]
    
    print("🎨 La Li Lu - Konwersja na PDF")
    print("=" * 40)
    
    for input_file, output_file in files_to_convert:
        if os.path.exists(input_file):
            convert_html_to_pdf(input_file, output_file)
        else:
            print(f"⚠️  Plik {input_file} nie istnieje, pomijam...")
    
    print("\n🎉 Konwersja zakończona!")
    print("📁 Pliki PDF zostały utworzone w bieżącym katalogu.")

if __name__ == "__main__":
    main() 