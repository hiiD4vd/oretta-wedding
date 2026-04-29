venues = [
    ("Mang Kabayan", "Rp24.000.000"),
    ("Ganesha", "Rp24.000.000"),
    ("RM Alam Pilemburan", "Rp24.000.000"),
    ("Kopi Tahura", "Rp24.000.000"),
    ("Airmen 25", "Rp24.000.000"),
    ("Nuuji", "Rp24.500.000"),
    ("Selasih", "Rp26.400.000"),
    ("Ngopdoel", "Rp26.400.000"),
    ("Paviliun Sunda", "Rp26.500.000"),
    ("Neka Coffee", "Rp28.150.000"),
    ("Kafe Kupu Kupu", "Rp28.400.000"),
    ("Luminor Hotel", "Rp28.800.000"),
    ("Tebu Hotel", "Rp28.800.000"),
    ("Fave Hper Square Paskal", "Rp28.800.000"),
    ("Lisung Dulang", "Rp28.850.000"),
    ("Pasar Baru Square", "Rp28.900.000"),
    ("Teras Ciseupan", "Rp29.300.000"),
    ("Puri 188", "Rp29.350.000"),
    ("Bahagia Kopi", "Rp31.800.000"),
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
    ("Selaras", "Rp41.900.000")
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
          <style>
            .venue-img { transition: transform 0.6s ease; }
            .venue-card-modern:hover .venue-img { transform: scale(1.08); }
            .venue-card-modern {
              background: var(--white);
              border-radius: 12px;
              overflow: hidden;
              box-shadow: 0 4px 15px rgba(0,0,0,0.05);
              transition: all 0.3s ease;
              cursor: pointer;
            }
            .venue-card-modern:hover {
              transform: translateY(-8px);
              box-shadow: 0 15px 30px rgba(0,0,0,0.1);
            }
            .venue-hidden { display: none !important; }
          </style>

          <div class="venue-list-container reveal-fade" style="padding: 2rem 0 4rem; margin-bottom: 2rem;">
            <div class="text-center" style="margin-bottom: 3rem;">
              <h3 style="font-family: var(--font-heading); font-size: clamp(1.8rem, 3vw, 2.5rem); color: var(--black); margin-bottom: 0.5rem;">Pilihan Paket Venue</h3>
              <p style="color: var(--text-dark); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Pilih venue impianmu. Semua paket sudah All-In 100 pax.</p>
            </div>
            
            <div id="venue-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 2rem;">"""

for i, v in enumerate(venues):
    name, price = v
    img = images[i % len(images)]
    hidden_class = " venue-hidden" if i >= 8 else ""
    
    card = f'''
              <div class="venue-card-modern{hidden_class}">
                <div style="width: 100%; height: 200px; overflow: hidden; position: relative;">
                  <img src="{img}" class="venue-img" style="width: 100%; height: 100%; object-fit: cover;" alt="{name}" />
                  <div style="position: absolute; top: 1rem; right: 1rem; background: var(--white); color: var(--black); font-size: 0.8rem; font-weight: bold; padding: 0.3rem 0.8rem; border-radius: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">ALL IN 100 PAX</div>
                </div>
                <div style="padding: 1.5rem; text-align: center;">
                  <h4 style="color: var(--black); margin: 0 0 0.5rem; font-family: var(--font-heading); font-size: 1.2rem;">{name}</h4>
                  <p style="color: var(--gold); margin: 0; font-weight: 700; font-size: 1.1rem;">{price}</p>
                </div>
              </div>'''
    html += card

html += """
            </div>
            
            <div class="text-center" style="margin-top: 3rem;">
              <button id="view-all-venues-btn" style="background: transparent; border: 2px solid var(--black); color: var(--black); padding: 0.8rem 2.5rem; font-size: 1rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; border-radius: 5px;">LIHAT SEMUA VENUE</button>
            </div>
            <div style="margin-top: 2rem; text-align: center;">
              <p style="font-size: 0.95rem; color: var(--text-dark); opacity: 0.8;">Detail request dan upgrade venue hubungi admin</p>
            </div>
          </div>

          <script>
            document.addEventListener('DOMContentLoaded', function() {
              const viewAllBtn = document.getElementById('view-all-venues-btn');
              const hiddenVenues = document.querySelectorAll('.venue-hidden');
              
              if(viewAllBtn) {
                viewAllBtn.addEventListener('click', function() {
                  const isHidden = hiddenVenues[0].style.display !== 'block';
                  
                  hiddenVenues.forEach(card => {
                    if (isHidden) {
                      card.style.display = 'block';
                      card.style.animation = 'fadeUp 0.5s ease forwards';
                    } else {
                      card.style.display = 'none';
                    }
                  });
                  
                  if (isHidden) {
                    viewAllBtn.innerText = 'SEMBUNYIKAN VENUE';
                    viewAllBtn.style.background = 'var(--black)';
                    viewAllBtn.style.color = 'var(--white)';
                  } else {
                    viewAllBtn.innerText = 'LIHAT SEMUA VENUE';
                    viewAllBtn.style.background = 'transparent';
                    viewAllBtn.style.color = 'var(--black)';
                  }
                });
              }
            });
          </script>"""

with open("d:\\daud\\projek bisnis\\oretta wedding\\venue_clean.txt", "w") as f:
    f.write(html)
