venues = [
    ("Mang Kabayan", "Rp24.000.000"),
    ("Ganesha", "Rp24.000.000"),
    ("RM Alam Pilemburan", "Rp24.000.000"),
    ("Kopi Tahura", "Rp24.000.000"),
    ("Airmen 25", "Rp24.000.000"),
    ("Ngopdoel", "Rp26.400.000"),
    ("Saoeng Paberik", "Rp32.400.000"),
    ("Atmosphere", "Rp33.800.000"),
    ("90 Gourment", "Rp33.850.000"),
    ("Dapoer Paberik", "Rp34.850.000"),
    ("Senusa", "Rp34.900.000"),
    ("Beehive", "Rp35.850.000"),
    ("Tjendana Bistro", "Rp36.900.000"),
    ("Kapulaga", "Rp38.300.000"),
    ("Nara Park", "Rp40.850.000"),
    ("Steikhaus", "Rp40.850.000"),
    ("Boda Barn", "Rp40.850.000"),
    ("Selaras", "Rp41.900.000"),
    ("Nuuji", "Rp24.500.000"),
    ("Bahagia Kopi", "Rp31.800.000"),
    ("Tebu Hotel", "Rp28.800.000"),
    ("Fave Hper Square Paskal", "Rp28.800.000"),
    ("Luminor Hotel", "Rp28.800.000"),
    ("Pasar Baru Square", "Rp28.900.000"),
    ("Selasih", "Rp26.400.000"),
    ("Paviliun Sunda", "Rp26.500.000"),
    ("Teras Ciseupan", "Rp29.300.000"),
    ("Puri 188", "Rp29.350.000"),
    ("Lisung Dulang", "Rp28.850.000"),
    ("Kafe Kupu Kupu", "Rp28.400.000"),
    ("Neka Coffee", "Rp28.150.000")
]

images = [
    "/images/portfolio_1.png",
    "/images/portfolio_2.png",
    "/images/portfolio_3.png",
    "/images/portfolio_4.png",
    "/images/portfolio_5.png",
    "/images/portfolio_6.png",
    "/images/wa_weddingplanner_639514205_18386872477153361_6399780977498644749_n.jpg",
    "/images/wa_weddingplanner_626624517_18384099499153361_494313317223290399_n.jpg"
]

html = """          <!-- Venue List -->
          <div class="venue-list-container reveal-fade" style="background: var(--black); color: var(--white); padding: 4rem 3rem; border-radius: 20px; margin-bottom: 4rem; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
            <h3 class="text-center" style="font-family: var(--font-heading); font-size: clamp(1.8rem, 3vw, 2.5rem); margin-bottom: 3rem; color: var(--gold);">PILIHAN PAKET VENUE INTIMATE</h3>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem; max-height: 80vh; overflow-y: auto; padding-right: 1rem; padding-bottom: 1rem;">"""

for i, v in enumerate(venues):
    name, price = v
    img = images[i % len(images)]
    card = f'''
              <div class="venue-card" style="position: relative; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.3); transition: transform 0.3s ease; cursor: pointer;">
                <img src="{img}" style="width: 100%; height: 280px; object-fit: cover; filter: brightness(0.8);" />
                <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); padding: 2rem 1rem 1rem;">
                  <h4 style="color: var(--white); margin: 0 0 0.2rem; font-family: var(--font-heading); font-size: 1.1rem; line-height: 1.2;">{name}</h4>
                  <p style="color: var(--gold); margin: 0; font-weight: 600; font-size: 1.2rem;">{price}</p>
                </div>
              </div>'''
    html += card

html += """
            </div>
            <div style="margin-top: 3rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
              <p style="font-family: var(--font-heading); font-size: 1.5rem; color: var(--gold); margin-bottom: 0.5rem; font-style: italic;">dengan banyaknya pilihan venue...</p>
              <p style="font-size: 1rem; color: rgba(255,255,255,0.7); letter-spacing: 1px;">Detail request dan upgrade venue hubungi admin</p>
            </div>
          </div>"""

with open("d:\\daud\\projek bisnis\\oretta wedding\\venue.txt", "w") as f:
    f.write(html)
