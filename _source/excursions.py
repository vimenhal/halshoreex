# Per-excursion data. Every string is copied verbatim from the live HAL pages
# (see ../../content-inventory.md). Only case and date/time formatting are normalised.
# Fields ending in _html may contain <b>, <a> and &amp; — everything else is plain text.

# Ship times are not on any live page. The API will provide them; until then every page uses this filler.
SHIP_TIMES_FILLER = {"arrive": "7:00 AM", "aboard": "5:00 PM"}

EXCURSIONS = [
  {
    "file": "seaplane-flight-fine-dining.html",
    "title": "Seaplane Flight & Fine Dining",
    "photo": "sydney-opera-house.webp", "focal": "53% 50%",
    "port": "Sydney, Australia", "port_short": "Sydney", "day": 37,
    "date": "Wed, Feb 10, 2027", "date_short": "Feb 10",
    "start": "10:30 AM", "duration": "5 hours",
    "adult": "$964.95", "child": None,
    "status": "limited", "badges": [],
    "activity": "Moderate", "wheelchair": None, "meals": "Meal provided",
    "language": "English",
    "notice": None,
    "top3": [
      "The experience and romance of a floatplane flight",
      "A bird's-eye view of Ku-Ring-Gai Chase National Park",
      "A memorable riverside lunch experience at Cottage Point Inn",
    ],
    "about_html": [
      "You're in for the thrill of a lifetime today as you enjoy the experience and romance of a floatplane flight.",
      "The aircraft takes off from beautiful Rose Bay and follows the coastline along Sydney's northern beaches, flying directly from Sydney Harbour to the tranquil waters of the Hawkesbury River and Ku-Ring-Gai Chase National Park.",
      "Turning inland over the majestic Ku-Ring-Gai Chase National Park and Hawkesbury River, you'll land in front of Cottage Point Inn — one of the Sydney area's best-kept secrets. Step out onto the restaurant's private jetty. The Cottage Point Inn features both indoor and outdoor seating. Enjoy superb modern Australian cuisine as you enjoy a leisurely three-hour lunch.",
      "Take time afterward to relax amid the sights and sounds of the Australian bush and birdlife.",
      "On the return flight to Sydney Harbour, your pilot will take you past the Harbour Bridge and Opera House before landing at Rose Bay — a truly spectacular way to end your riverside lunch experience.",
      "Transfer back to the ship by coach.",
    ],
    "notes_html": [
      "Maximum weight is 280 lbs. Not advisable for guests using a wheelchair. Mobility devices (wheelchairs, walkers, scooters, etc) cannot be accommodated on the aircraft. Tour does not operate on Mondays, Tuesdays or holidays.",
    ],
  },
  {
    "file": "easter-island-panorama.html",
    "title": "Easter Island Panorama",
    "photo": "easter-island-moai.webp", "focal": "60% 50%",
    "port": "Easter Island, Chile", "port_short": "Easter Island", "day": 16,
    "date": "Wed, Jan 20, 2027", "date_short": "Jan 20",
    "start": "10:00 AM", "duration": "3 hours",
    "adult": "$299.95", "child": None,
    "status": None, "badges": [],
    "activity": "Moderate", "wheelchair": None, "meals": None,
    "language": "English",
    "notice": None,
    "top3": [
      "Easter Island's mystical Moai statues",
      "A stop at the handicraft market",
      "The archaeological site of Ahu Akivi",
    ],
    "about_html": [
      "Leaving the harbor of Hanga Piko, your coach drives through the village of Hanga Roa.",
      "At the ceremonial site of Tahai, located on the west coast of the island, you will see altars and the monolithic Moai statues that have become an iconic symbol of Rapa Nui culture.",
      "A stop at the handicrafts market allows you some time to admire some of the crafts in wood and shell made by the islanders.",
      "Leave the village and relax during a 20-minute drive to the archaeological site of Ahu Akivi, featuring seven restored statues. Hear the legend and lore surrounding these statues, which represent the seven ambassadors sent to Easter Island by King Hotu Matua.",
      "Then, enjoy a scenic drive back to the pier with a short photo stop at Ahu Poukura — an unrestored statue.",
    ],
    "notes_html": [
      "Minimum age is 12 years. Easter Island has a hot and humid climate. Shade is limited; to avoid sunburn, wear light, long clothing suitable for use as a cover-up. Bring a hat and sunglasses, wear biodegradable sunscreen. Bring bottled water. Wear comfortable walking shoes. Tourism infrastructure is very limited on Easter Island. Transportation will be by way of several different types of vehicles, including minibuses and vans. A guide waits for you at each point of interest and provides narration and explanation, rather than riding with you in the vehicle. The ship is at anchor on Easter Island, and the Immigration clearance process can take more than an hour. Having your immigration card filled out prior to arrival will expedite the process. Very few vendors on Easter Island accept credit cards; bring US dollars or Chilean pesos. Mobility devices (wheelchairs, walkers, scooters, etc) cannot be accommodated on the transportation. Participants must be able to climb a few steps unassisted to board the transportation.",
    ],
  },
  {
    "file": "accessible-lisbon-jeronimos-monastery.html",
    "title": "Accessible Lisbon & Jeronimos Monastery",
    "photo": "lisbon-jeronimos.webp", "focal": "42% 50%",
    "port": "Lisbon, Portugal", "port_short": "Lisbon", "day": 104,
    "date": "Sun, Apr 18, 2027", "date_short": "Apr 18",
    "start": "9:00 AM", "duration": "4 hours",
    "adult": "$299.95", "child": None,
    "status": "soldout", "badges": ["ats"],
    "activity": "Easy",
    "wheelchair": "Accessible to guests using a wheelchair. Transportation features lift equipment and storage space for wheelchairs. All venues are accessible with ramps and/or elevators.",
    "meals": None,
    "language": "English",
    "notice": "This tour is the wheelchair accessible version of the standard tour for this port. Only guests using a wheelchair should book this tour as it ensures accessible transportation. If you or anyone in your party do not require the use of a wheelchair during the tour, please book the standard tour option. Bookings with the accessibility requirement will be verified onboard.",
    "top3": [
      "The vibrant Baixa area; the fortified Tower of Belem",
      "The Nossa Senhora do Monte viewpoint",
      "The UNESCO World Heritage Site Jeronimos Monastery",
    ],
    "about_html": [
      "This tour is designed to be accessible for all guests, including those using a wheelchair. Explore Lisbon and its amazing historical sites along the Tagus River for perhaps the perfect overview of Portugal's charming capital city.",
      "Meet your guide and accessible van and head out on a scenic panoramic drive through the heart of Lisbon. Encounter the vibrant commercial and historic Baixa area, peppered with Portugal's neo-Classical architecture, bustling, pedestrianized streets, and trendy shops.",
      "You will also see Lisbon's Lower Town, the Santa Justa Lift, and Rossio Square. Discover historical streets, traditional shops, iconic squares and ornate churches — weathervanes pointing to a prosperous past. Taste the famous ginjinha — Lisbon's cherry liqueur.",
      "In the Belém Quarter, pay homage to the Portuguese Discoveries period. You will see the Tagus River — the embarkation point for Vasco de Gama's great discoveries — and the iconic Monument to the Discoveries, the 25th April Bridge, and the Palácio de São Bento, home to the Portuguese Parliament. The fortified Tower of Belém is one of Lisbon's postcard landmarks.",
      "Your tour continues to the UNESCO World Heritage Site Jerónimos Monastery. Here, you will visit Santa Maria Church of the Jeronimos. Note the fascinating and fabulous Gothic-Manueline architecture that resulted from Portugal's immense trade wealth.",
      "Return to the pier with a drive along the River Tagus and a view of the April 25 Bridge, Christ the King statue, and Praça do Comercio — the largest square in Europe.",
    ],
    "notes_html": [
      "This tour is designed to be accessible for all guests, including those using a wheelchair (the tour operator suggests you bring a companion to assist, as guides are not allowed to push wheelchairs). Companions can book the same tour under the title Accessible Lisbon &amp; Jeronimos Monastery (Companion). Jeronimos Church is closed on Mondays and National Holidays. A visit to the Church of Sao Domingo will be substituted for Jeronimos Church on Mondays. The tour route avoids stairs; however, the nature of access may differ from the standards you are familiar with at home. Some sections of the route may have uneven surfaces or cobblestones. There is also a small step of approximately 3cm at the entrance to San Jeronimos Church that must be navigated. Accessible bathrooms with wide doors are available along the tour route. An accessible vehicle with a wheelchair lift or ramp is used for transportation. The number of accessible vehicles available is extremely limited; make your accessible shore excursion reservations as far in advance as possible. Guests requiring accessible transportation, please complete the Special Services form at <a href=\"https://book.hollandamerica.com/specialServices/login.action\">https://book.hollandamerica.com/specialServices/login.action</a>; this will ensure that suitable transportation is in place for your tour.",
    ],
  },
  {
    "file": "kings-vikings-roskilde.html",
    "title": "Kings & Vikings: The Viking Ship Museum & Roskilde Cathedral curated with The HISTORY Channel",
    "photo": "roskilde-cathedral.webp", "focal": "50% 50%",
    "port": "Copenhagen, Denmark", "port_short": "Copenhagen", "day": 116,
    "date": "Fri, Apr 30, 2027", "date_short": "Apr 30",
    "start": "10:30 AM", "duration": "4.5 hours",
    "adult": "$189.95", "child": "$159.95",
    "status": None, "badges": ["history"],
    "activity": "Moderate", "wheelchair": None, "meals": None,
    "language": "English",
    "notice": None,
    "top3": [
      "The Viking Ship Museum and Museum Island",
      "An archaeology workshop; Viking ship replicas",
      "Roskilde Cathedral — a UNESCO World Heritage Site",
    ],
    "about_html": [
      "Curated with the History Channel, uncover the Viking and Hanseatic legacy of Roskilde, an ancient hub of trade and power.",
      "Begin at the Viking Ship Museum, home to five Viking longboats excavated from Roskilde Fjord. These ships highlight Roskilde's maritime importance during the Viking Age, connecting Scandinavia to the Hanseatic League's expansive trade and bargaining network.",
      "Outside, watch master craftsmen recreate Viking-age ships using traditional techniques, keeping alive the skills that once supported international commerce.",
      "Next, visit Roskilde Cathedral, Scandinavia's earliest brick Gothic cathedral and a UNESCO World Heritage Site. Built in the 12th century, the cathedral reflects Roskilde's historical prominence in trade and religion. Danish monarchs, including Harald Bluetooth, rest here in ornate tombs. Admire the bronze statues, frescoes, and wooden choir stalls depicting scenes of creation and judgment, symbolic of Denmark's cultural and trade ties within the Hanseatic world.",
    ],
    "notes_html": [
      "Terrain includes surfaces at the museum. Inside church visit(s) may not be possible if religious services are being held or if precluded by time constraints. Minimum age is 10 years.",
      "Shore excursions and programming are not sponsored or administered by The History Channel ™ and are offered and administered exclusively by Holland America",
    ],
  },
  {
    "file": "hidden-lanzarote.html",
    "title": "Hidden Lanzarote",
    "photo": "lanzarote-cactus-garden.webp", "focal": "57% 50%",
    "port": "Arrecife, Lanzarote, Canary Islands, Spain", "port_short": "Arrecife", "day": 100,
    "date": "Wed, Apr 14, 2027", "date_short": "Apr 14",
    "start": "9:15 AM", "duration": "4 hours",
    "adult": "$89.95", "child": "$69.95",
    "status": None, "badges": [],
    "activity": "Moderate", "wheelchair": None, "meals": None,
    "language": "English",
    "notice": None,
    "top3": [
      "Teguise -- former capital of Lanzarote",
      "Cesar Manrique's Jardin de Cactus",
      "An aloe vera farm",
    ],
    "about_html": [
      "Depart the pier on a scenic drive north to see Lanzarote's historic former capital of Teguise.",
      "En route, you'll pause at the Haria Viewpoint for breathtaking vistas of the northern headland and neighboring islands.",
      "Continue to the village of Punta Mujeres to visit an aloe vera farm, where you'll learn about the numerous uses for aloe and what makes this island such an excellent spot for farming it. You'll also have the opportunity to try some aloe juice and see how the plant is cultivated.",
      "Head to Cesar Manrique's Jardin de Cactus -- home to more than 1,500 cacti of at least 100 different species found in Lanzarote, America and Madagascar. Take time to stroll around this unusual and beautiful garden before concluding your tour with the return drive to the pier.",
    ],
    "notes_html": [
      "This tour does not operate on Sundays. Shade is limited; to avoid sunburn, wear light, long clothing suitable for use as a cover-up. Bring a hat and sunglasses; wear biodegradable sunscreen. Bring bottled water.",
    ],
  },
  {
    "file": "tahiti-lagoon-discovery.html",
    "title": "Tahiti Lagoon Discovery",
    "photo": "tahiti-lagoon.webp", "focal": "49% 50%",
    "port": "Papeete, French Polynesia", "port_short": "Papeete", "day": 22,
    "date": "Tue, Jan 26, 2027", "date_short": "Jan 26",
    "start": "8:30 AM", "duration": "3 hours",
    "adult": "$139.95", "child": "$114.95",
    "status": None, "badges": [],
    "activity": "Moderate", "wheelchair": None, "meals": None,
    "language": "English",
    "notice": None,
    "top3": [
      "A swim adventure in clear water",
      "Anchor in the lagoon for time in the water",
      "Watching for dolphins, often seen in this area",
    ],
    "about_html": [
      "Step aboard a <b>boat</b> and head to the <b>west coast of Tahiti</b>, enjoying views of the mountains and the island's shoreline.",
      "Your captain will anchor in the lagoon. Be ready to jump in and discover the spectacular marine life of the Society Islands, including sandy and coral areas.",
      "As you <b>swim</b>, keep your eyes peeled for dolphins, often seen in the area.",
    ],
    "notes_html": [
      "Itinerary and stops may be reduced or may differ dependent upon weather conditions. Participants must know how to swim and be comfortable wearing snorkeling equipment, being in deep water and coping with occasional currents. Participants may remain on the boat, but viewing will be limited. Do not touch or step on the coral or touch marine animals. Wildlife sightings are likely but are not guaranteed. Sailing on board a boat requires vigilance; participants must be physically and mentally alert to the boating environment and fit enough to negotiate steps and the vessel layout. Wear your swimsuit under your clothing; bring a towel, reef-safe/biodegradable sunscreen, light clothing to act as a full cover-up for further protection from the sun, and a hat. Swim at your own risk. Mask and snorkel provided. Not advisable for guests using a wheelchair or for those with mobility limitations.",
    ],
  },
  {
    # Live page badge reads "1 Spots Left" -> status "spots" with the count (user, 2026-11-04: live counts are OK).
    # Meals: no "Includes" fact on the live page, but Top 3 and the description say snacks and
    # beverages are served, so the tile says "Snack provided" (API meals value Snack) — confirmed by user.
    "file": "kauai-hiking-adventure.html",
    "title": "Kauai Hiking Adventure",
    "photo": "kauai-napali-coast.webp", "focal": "68% 50%",
    "port": "Nawiliwili, Kauai, Hawaii, US", "port_short": "Nawiliwili", "day": 7,
    "date": "Mon, Feb 1, 2027", "date_short": "Feb 1",
    "start": "8:30 AM", "duration": "4.5 hours",
    "adult": "$199.95", "child": None,
    "status": "spots", "spots": 1, "badges": [],
    "activity": "Strenuous", "wheelchair": None, "meals": "Snack provided",
    "language": "English",
    "notice": None,
    "top3": [
      "Kauai's only hike dedicated to cruise line guests",
      "A chance to breathe in the beautiful Halelea Forest Reserve",
      "Snacks and beverages at the Keahua Arboretum",
    ],
    "about_html": [
      "Join this amazing hiking adventure in the heart of the Kauai forest. Some stunning views make it a very memorable experience.",
      "Begin with a short drive to Opaeka'a Falls and the Waimea River, stopping en route for an introduction to Kauai's culture.",
      "Another short drive brings you to a trailhead leading into the dark and mighty Halelea Forest Reserve. Garden Isle foliage, fauna and legends accompany you all along the way.",
      "After the hike, return to the van and take another short drive to the Keahua Arboretum for snacks and beverages, concluding your journey with a relaxing drive back to the ship.",
    ],
    "notes_html": [
      "Minimum age is 8 years. Participants must be able to hike four miles unassisted. Terrain is moderate but can be slippery and muddy when wet. Showers are frequent; bring a raincoat. Wear sturdy, non-skid, closed-toe walking/hiking shoes (mandatory); clothing and shoes may get muddy in rainy conditions. Tour operates rain or shine, but may be canceled by the operator in the event of extremely bad weather or unsuitable conditions. The hike is 2.1 miles each way; 4.2 miles round trip. Tour does not operate on weekends.",
    ],
  },
]

# ── Shared copy (every page) ──
BADGES = {
  "history": {"label": "HISTORY Channel Exclusive", "icon": "i-award", "img": "history-h.png"},
  "ats":     {"label": "Accessible Travel Solutions Exclusive", "icon": "i-spark"},
  "heritage": {"label": "Heritage Tour", "icon": "i-landmark"},
}
STATUS = {"limited": "Limited Capacity", "soldout": "Sold Out"}

ACTIVITY_LEVELS = [
  ("Easy", "Very light activity including short distances to walk; may include steps."),
  ("Moderate", "Requires intermittent effort throughout, including walking medium distances over uneven surfaces and/or steps."),
  ("Strenuous", "Requires active participation, walking long distances over uneven and steep terrain or on steps. In certain instances, paddling or other non-walking activity is required, and guests must be able to participate without discomfort or difficulty breathing."),
]

CANCELLATION_HTML = [
  "Online cancellations will not be accepted during the 3-day period prior to cruise departure. Instead, you will need to cancel once you board the ship. All onboard cancellations are subject to at least a 10% cancellation fee. If you cancel a Signature Collection Shore Excursions within 3 days of sailing, a 100% cancellation fee will apply since transportation and services will have already been arranged with the appropriate Shore Excursion operator. If cancellation occurs onboard after the cancellation deadline for a specific Shore Excursion, a 100% cancellation fee will apply. The ship's Shore Excursions Office will be able to advise you of the cancellation deadline applicable to each Shore Excursion. Passengers who wish to cancel should visit the Shore Excursions Office upon embarkation. Optional Shore Excursions during the land portion of an Alaska Land+Sea Journey are non-refundable within 3 days of your Land+Sea Journey departure date.",
  "In the case of online cancellations made by you (which cannot be made during the 3-day period prior to cruise departure) or cancellations made by us more than 3 days prior to cruise departure, we will issue a credit on the credit card that was used to pay for the booking. For all other cancellations (whether by you, Holland America Line or the Shore Excursion operator), a credit will not be given on your credit card. Instead, we will apply an ONBOARD CREDIT ONLY policy under which the refund (less any cancellation fee) will show up as a credit to the shipboard account of the person who was to take the Shore Excursion. If the credit is not fully utilized during the cruise, the balance will be paid to that passenger by the ship's Purser at the end of the voyage.",
]

# (question, [paragraph html] or {"list": [...]})
FAQ = [
  ("What are Shore Excursions?", ["Shore excursions are available through our partnerships with local suppliers and guides, in the majority of ports we visit. They cover an amazing array of places, landmarks, activities and experiences — from wildlife encounters in the Outback and salsa lessons in Havana to wine-tastings on a French estate and zip-lining in the Costa Rican rainforest. We offer something for every interest, taste and capability level."]),
  ("What are the benefits of booking shore excursions?", {"list": [
    "Guaranteed best price — find a better price on any tour we offer and we'll refund you 100 percent of the price difference in the form of an onboard credit. More information available at Best Price Guarantee",
    "Earlier departure off the ship",
    "Guaranteed return to the ship",
    "Licensed, insured and professional local operators &amp; Guides",
    "Full refund if the port is missed",
    "Flexibility to cancel up to 24 hours prior",
    "Expert advice offered pre-cruise by our dedicated call center and onboard by our shore excursion staff",
  ]}),
  ("How do I book shore excursions?", [
    "We recommend you book early for the best selection, as our excursions and tours have limited capacity and fill up quickly. If tour details are not yet finalized, please check again closer to your departure date. Shore excursions may be booked and prepaid online up to three days before sailing. Your Digital Tour Tickets will be available under My Account in Navigator. Please download the Navigator app prior to boarding. You will also be able to request tours on the ship at the shore excursion Office.",
    "Many tours have limited availability, and booking tours in advance reduces the chance of disappointment. All tour bookings are processed on a first-come, first-served basis. Prices are subject to change without notice. Tours are booked and paid with a credit card and a confirmation will be sent to your email address. If a tour is sold out, many tours offer a waitlist option. If a tour is waitlisted and space becomes available, an email notification will be sent to you at which time you will have 72 hours to book and confirm the tour. Your credit card will be charged once you have confirmed your tour.",
  ]),
  ("Is there a dedicated resource I can speak with about shore excursions?", [
    "The shore excursion reservation office is available to assist you Monday-Friday, 7 AM to 4 PST. Guests may call <a href=\"tel:18884259376\">1 (888) 425-9376</a> to speak directly with an agent.",
  ]),
  ("What is the timing of shore excursions?", [
    "Shore excursion departure times coincide with the ship's schedule as well as other tours, enabling you to take multiple tours if desired with worry-free return to the ship. In the very rare event that your tour is late and the ship must leave, we will arrange at our expense to get you to the next port of call. With independently booked tours, you are responsible for rejoining the ship at the next port of call.",
  ]),
  ("Does Holland America Line offer accessible shore excursions?", [
    "Holland America Line is committed to providing safe, easy, and accessible accommodations for all persons with disabilities, to the extent that is feasible. The tours are graded according to their relative level of activity. The activity icons that appear at the beginning of each tour description provide a general idea of the level of activity to expect. It is important to keep in mind that tour operators are subject to the laws of their own country with respect to accommodating the needs of guests with disabilities. In most foreign countries, the laws are not as stringent as those in the United States. We cannot guarantee that all are able to provide facilities that are accessible to individuals with disabilities and third party shore excursion facilities may not be fully accessible to guests with disabilities. For detailed information on accessibility of shore excursions, we strongly recommend contacting our shore excursions reservations department well in advance of embarkation at <a href=\"tel:18884259376\">1-888-425-9376</a> (or locally at <a href=\"tel:2066267320\">206-626-7320</a>). Once onboard, please visit the shore excursions office.",
  ]),
  ("What are the cancellation policies for shore excursions?", [
    "Cancellations for pre-paid tours are allowed up to 3 days prior to cruise embarkation and will be refunded to the credit card used for the purchase. If within 3 days of embarkation, all changes/cancellations must be done onboard the ship and refunds will be applied to your onboard account. If the credit is not fully utilized during the cruise, the balance will be paid to that passenger by the ship's Purser at the end of the voyage. If cancellation occurs onboard after the cancellation deadline for specific shore excursions, a 100% cancellation fee will apply. The ship's shore excursions office will be able to advise you of the cancellation deadline applicable to each tour. Optional shore excursions during the land portion of a Land &amp; Sea Journey are non-refundable within 3 days of your Land &amp; Sea Journey departure date. Group shore excursions cancelled within three days prior to embarkation (sail) date are nonrefundable. Custom tours may have different cancellation deadlines which will be stated in the proposal. In the rare instance that tours are cancelled by Holland America Line or the tour operator, the full amount will be refunded within four to six weeks after the voyage ends.",
  ]),
]
