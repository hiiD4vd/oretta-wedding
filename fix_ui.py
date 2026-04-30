import os

base_dir = r'd:\daud\projek bisnis\oretta wedding'
files = [
    os.path.join(base_dir, 'index.html'),
    os.path.join(base_dir, 'venue.html')
]

for path in files:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix copywriting
    content = content.replace('cuma 24jt aja🥺', 'Mulai dari Rp24.000.000,-')
    content = content.replace('Hand bouqet', 'Hand bouquet')

    # Fix dead links in portfolio
    content = content.replace('href="#" class="grid-item"', 'href="javascript:void(0)" class="grid-item"')
    content = content.replace('href="#"', 'href="javascript:void(0)"')
    
    # Pre-fill WhatsApp link if not already done
    wa_base = 'https://wa.me/6285973929029'
    wa_text = '?text=Halo%20Admin%20Oretta,%20saya%20ingin%20konsultasi%20mengenai%20Wedding%20Package'
    
    # Simple replacement, we assume it's just href="https://wa.me/..."
    content = content.replace('href="https://wa.me/6285973929029"', f'href="{wa_base}{wa_text}"')

    # Fix venue grid column inline styling to use class for mobile query
    content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;"', 'class="venue-grid-container"')
    
    content = content.replace('style="width: 100%; height: 350px; overflow: hidden; position: relative;"', 'class="venue-img-wrapper"')

    # Add reveal-fade to venue-card-modern
    content = content.replace('class="venue-card-modern"', 'class="venue-card-modern reveal-fade"')
    
    # Prevent duplicate reveal-fades if it was already added
    content = content.replace('reveal-fade reveal-fade', 'reveal-fade')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print('HTML structure fixed')
