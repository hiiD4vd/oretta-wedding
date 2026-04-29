with open("d:\\daud\\projek bisnis\\oretta wedding\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "          <!-- Venue List -->"
end_marker = "          <div class=\"text-center reveal-fade\">"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    with open("d:\\daud\\projek bisnis\\oretta wedding\\venue_clean.txt", "r", encoding="utf-8") as f:
        new_venue = f.read()
    
    new_content = content[:start_idx] + new_venue + "\n" + content[end_idx:]
    
    with open("d:\\daud\\projek bisnis\\oretta wedding\\index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced venue list.")
else:
    print("Markers not found.")
