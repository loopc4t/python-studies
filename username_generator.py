import random

adjectives = [
    # Sonic characteristics
    'Harsh', 'Abrasive', 'Distorted', 'Chaotic', 'Brutal', 'Raw', 'Dense', 
    'Saturated', 'Static', 'Violent', 'Oppressive', 'Grinding', 'Piercing',
    'Crushing', 'Rusted', 'Corroded', 'Fractured', 'Shattered', 'Warped',
    'Molten', 'Scorched', 'Frozen', 'Numb', 'Caustic', 'Acidic', 'Searing',
    'Blistering', 'Scalding', 'Charred', 'Incinerated', 'Scorched', 'Smoldering',
    
    # Anti-musical
    'Atonal', 'Arrhythmic', 'Formless', 'Structureless', 'Dissonant',
    'Unmelodic', 'Broken', 'Fragmented', 'Dismantled', 'Eroded', 'Collapsed',
    'Ruptured', 'Severed', 'Torn', 'Ripped', 'Split', 'Cracked',
    
    # Conceptual/dark
    'Transgressive', 'Nihilistic', 'Deviant', 'Void', 'Abyssal', 'Terminal',
    'Condemned', 'Rejected', 'Forbidden', 'Oblique', 'Cryptic', 'Occult',
    'Spectral', 'Phantom', 'Hollow', 'Vacant', 'Barren', 'Sterile', 'Desolate',
    'Forsaken', 'Abandoned', 'Cursed', 'Damned', 'Doomed', 'Blighted',
    'Plagued', 'Infected', 'Rotten', 'Putrid', 'Fetid', 'Rank', 'Foul',
    
    # Physical/visceral
    'Bleeding', 'Wounded', 'Scarred', 'Mangled', 'Twisted', 'Contorted',
    'Convulsed', 'Spasmic', 'Trembling', 'Shuddering', 'Pulsing', 'Throbbing',
    'Aching', 'Sore', 'Bruised', 'Lacerated', 'Mutilated', 'Disfigured',
    'Severed', 'Amputated', 'Eviscerated', 'Gutted', 'Flayed', 'Skinned',
    
    # Industrial/mechanical
    'Industrial', 'Mechanical', 'Synthetic', 'Artificial', 'Metallic',
    'Concrete', 'Iron', 'Steel', 'Toxic', 'Septic', 'Necrotic', 'Galvanized',
    'Chrome', 'Aluminum', 'Copper', 'Brass', 'Zinc', 'Lead', 'Mercury',
    'Asbestos', 'Pneumatic', 'Hydraulic', 'Electric', 'Magnetic', 'Radioactive',
    
    # Textural
    'Granular', 'Crystalline', 'Viscous', 'Coarse', 'Jagged', 'Serrated',
    'Angular', 'Splintered', 'Razored', 'Bladed', 'Sharp', 'Pointed', 'Barbed',
    'Thorned', 'Spiked', 'Hooked', 'Clawed', 'Fanged', 'Toothed',
    
    # Emotional/psychological
    'Anguished', 'Tormented', 'Afflicted', 'Deranged', 'Manic', 'Fevered',
    'Delirious', 'Catatonic', 'Comatose', 'Paralyzed', 'Traumatized', 'Shocked',
    'Stunned', 'Dazed', 'Confused', 'Disoriented', 'Hysteric', 'Panic',
    'Anxious', 'Paranoid', 'Schizoid', 'Psychotic', 'Neurotic', 'Obsessive',
    
    # Temperature/sensation
    'Glacial', 'Arctic', 'Subzero', 'Frigid', 'Icy', 'Frostbitten',
    'Burning', 'Blazing', 'Infernal', 'Volcanic', 'Thermal', 'Heated',
    
    # Motion/energy
    'Convulsive', 'Seismic', 'Tectonic', 'Kinetic', 'Dynamic', 'Volatile',
    'Unstable', 'Erratic', 'Sporadic', 'Random', 'Chaotic', 'Turbulent',
    
    # Decay/time
    'Ancient', 'Primordial', 'Archaic', 'Antique', 'Aged', 'Weathered',
    'Decayed', 'Decomposed', 'Degraded', 'Deteriorated', 'Withered', 'Wilted',
    
    # Light/dark
    'Black', 'Obsidian', 'Onyx', 'Jet', 'Sable', 'Pitch', 'Umbral',
    'Shadow', 'Dark', 'Dim', 'Murky', 'Opaque', 'Obscure',
    
    # Intensity
    'Extreme', 'Intense', 'Maximum', 'Total', 'Complete', 'Absolute',
    'Pure', 'Utter', 'Sheer', 'Raw', 'Primal', 'Savage', 'Feral', 'Wild',
    
    # Negative states
    'Dead', 'Dying', 'Moribund', 'Lifeless', 'Inanimate', 'Inert',
    'Dormant', 'Latent', 'Silent', 'Mute', 'Deaf', 'Blind', 'Numb',

    # Ambient / atmospheric
    'Ethereal', 'Airy', 'Weightless', 'Subtle', 'Soft', 'Drifting', 'Floating',
    'Luminescent', 'Resonant', 'Harmonic', 'Echoing', 'Reverberant', 'Hazy',
    'Distant', 'Infinite', 'Boundless', 'Transparent', 'Diffuse', 'Vaporous',
    'Dreamlike', 'Somnolent', 'Hypnotic', 'Mesmeric', 'Meditative', 'Tranquil',
    'Serene', 'Calm', 'Still', 'Silent', 'Nocturnal', 'Twilight', 'Liminal',

    # Surreal / abstract
    'Hallucinatory', 'Oneiric', 'Phantasmagoric', 'Disjointed', 'Elastic',
    'Melting', 'Shifting', 'Fluid', 'Bizarre', 'Uncanny', 'Paradoxical',
    'Nonlinear', 'Fragmentary', 'Irrational', 'Subconscious', 'Illusory',
    'Kaleidoscopic', 'Distorted', 'Twisted', 'Dreamlike',

    # Avant-garde / artistic
    'Minimalist', 'Conceptual', 'Improvised', 'Abstract', 'Experimental',
    'Deconstructive', 'Textural', 'Gestural', 'Tonal', 'Microtonal',
    'Aleatoric', 'Serial', 'Dissonant', 'Postmodern', 'Expressionist',
    'Dadaist', 'Futurist', 'Surrealist', 'Fluxus', 'Absurd', 'Provocative',
    'Radical', 'Subversive', 'Disruptive', 'Unorthodox', 'Oblique', 'Instinctive',

    # Cinematic / emotional
    'Cinematic', 'Visual', 'Vivid', 'Atmospheric', 'Epic', 'Minimal',
    'Grand', 'Introspective', 'Brooding', 'Melancholic', 'Somber', 'Tender',
    'Fragile', 'Delicate', 'Nostalgic', 'Bittersweet', 'Poetic', 'Contemplative',
    'Suspenseful', 'Tense', 'Haunting', 'Eerie', 'Mystical', 'Otherworldly',
    'Sacred', 'Ritualistic', 'Mythic', 'Ancient', 'Timeless', 'Eternal',

    # Organic / naturalistic
    'Organic', 'Pastoral', 'Earthy', 'Elemental', 'Fluid', 'Naturalistic',
    'Breathing', 'Flowing', 'Growing', 'Evolving', 'Mutable', 'Transient',

    # Sensory / perception
    'Auditory', 'Visual', 'Textural', 'Tactile', 'Sensual', 'Synesthetic',
    'Vibrant', 'Iridescent', 'Prismatic', 'Colorless', 'Monochrome',

    # “Raw” / primitive
    'Instinctual', 'Primal', 'Primitive', 'Visceral', 'Rough', 'Unfiltered',
    'Unrefined', 'Improvised', 'Unprocessed', 'Direct', 'Intuitive', 'Crude'
]

nouns = [
    # Electronic/equipment
    'Oscillator', 'Circuit', 'Feedback', 'Static', 'Signal', 'Frequency',
    'Voltage', 'Amplifier', 'Generator', 'Transmitter', 'Modulator',
    'Synthesizer', 'Reverb', 'Delay', 'Distortion', 'Filter', 'Processor',
    'Speaker', 'Microphone', 'Cable', 'Jack', 'Socket', 'Terminal', 'Node',
    'Transistor', 'Capacitor', 'Resistor', 'Diode', 'Relay', 'Switch',
    'Fuse', 'Coil', 'Magnet', 'Dynamo', 'Motor', 'Rotor', 'Stator',
    
    # Industrial/mechanical
    'Machine', 'Factory', 'Furnace', 'Turbine', 'Engine', 'Piston',
    'Grinder', 'Crusher', 'Conveyor', 'Assembly', 'Apparatus', 'Device',
    'Mechanism', 'Contraption', 'Steel', 'Metal', 'Iron', 'Concrete',
    'Foundry', 'Forge', 'Anvil', 'Hammer', 'Press', 'Drill', 'Lathe',
    'Mill', 'Saw', 'Cutter', 'Welder', 'Rivet', 'Bolt', 'Screw', 'Gear',
    'Wheel', 'Axle', 'Shaft', 'Bearing', 'Pulley', 'Chain', 'Belt',
    'Valve', 'Pump', 'Compressor', 'Tank', 'Barrel', 'Drum', 'Canister',
    
    # Body/visceral
    'Flesh', 'Bone', 'Marrow', 'Sinew', 'Tendon', 'Nerve', 'Vein',
    'Organ', 'Tissue', 'Membrane', 'Cortex', 'Spine', 'Skull', 'Jaw',
    'Tooth', 'Claw', 'Fang', 'Lung', 'Heart', 'Brain', 'Eye', 'Ear',
    'Mouth', 'Throat', 'Stomach', 'Gut', 'Liver', 'Kidney', 'Blood',
    'Muscle', 'Skin', 'Hair', 'Nail', 'Rib', 'Pelvis', 'Femur', 'Vertebra',
    
    # Nature/elemental
    'Void', 'Abyss', 'Chasm', 'Fissure', 'Crevice', 'Crater', 'Trench',
    'Storm', 'Tempest', 'Cyclone', 'Vortex', 'Maelstrom', 'Avalanche',
    'Quake', 'Tremor', 'Eruption', 'Magma', 'Lava', 'Ash', 'Frost',
    'Thunder', 'Lightning', 'Hail', 'Blizzard', 'Tornado', 'Hurricane',
    'Tsunami', 'Flood', 'Drought', 'Fire', 'Smoke', 'Ember', 'Cinder',
    'Ice', 'Snow', 'Sleet', 'Rain', 'Mist', 'Fog', 'Cloud', 'Wind',
    
    # Abstract/conceptual
    'Ritual', 'Ceremony', 'Rite', 'Doctrine', 'Manifesto', 'Testament',
    'Transmission', 'Broadcast', 'Emission', 'Discharge', 'Radiation',
    'Decay', 'Entropy', 'Dissolution', 'Erosion', 'Corrosion', 'Rust',
    'Plague', 'Virus', 'Infection', 'Disease', 'Fever', 'Malady', 'Affliction',
    'Curse', 'Hex', 'Spell', 'Charm', 'Sigil', 'Glyph', 'Rune', 'Symbol',
    
    # Death/dark
    'Crypt', 'Tomb', 'Grave', 'Coffin', 'Morgue', 'Autopsy', 'Corpse',
    'Cadaver', 'Remains', 'Wreckage', 'Ruin', 'Debris', 'Rubble', 'Ash',
    'Cemetery', 'Mausoleum', 'Sepulcher', 'Burial', 'Funeral', 'Wake',
    'Shroud', 'Casket', 'Urn', 'Pyre', 'Cremation', 'Incineration',
    
    # Architecture/space
    'Bunker', 'Silo', 'Tower', 'Monolith', 'Obelisk', 'Vault', 'Chamber',
    'Corridor', 'Shaft', 'Duct', 'Tunnel', 'Catacomb', 'Labyrinth', 'Maze',
    'Prison', 'Cell', 'Dungeon', 'Cage', 'Pit', 'Well', 'Cistern',
    'Warehouse', 'Depot', 'Hangar', 'Garage', 'Station', 'Terminal',
    'Platform', 'Bridge', 'Causeway', 'Passage', 'Gateway', 'Portal',
    
    # Weapons/violence
    'Blade', 'Razor', 'Scalpel', 'Needle', 'Wire', 'Spike', 'Barb',
    'Shard', 'Splinter', 'Fragment', 'Shrapnel', 'Bullet', 'Shell',
    'Knife', 'Dagger', 'Sword', 'Axe', 'Mace', 'Flail', 'Spear', 'Lance',
    'Arrow', 'Bolt', 'Dart', 'Javelin', 'Harpoon', 'Trident', 'Pike',
    
    # Medical/clinical
    'Surgery', 'Incision', 'Laceration', 'Trauma', 'Wound', 'Lesion',
    'Infection', 'Contamination', 'Toxin', 'Virus', 'Plague', 'Pathogen',
    'Specimen', 'Sample', 'Vial', 'Syringe', 'Scalpel', 'Forceps', 'Clamp',
    'Suture', 'Bandage', 'Gauze', 'Swab', 'Probe', 'Catheter', 'Tube',
    
    # Time/decay
    'Epoch', 'Era', 'Cycle', 'Phase', 'Terminal', 'Collapse', 'Extinction',
    'End', 'Finale', 'Death', 'Demise', 'Doom', 'Fate', 'Destiny',
    'Oblivion', 'Annihilation', 'Apocalypse', 'Armageddon', 'Cataclysm',
    
    # Chemicals/materials
    'Acid', 'Alkali', 'Solvent', 'Reagent', 'Catalyst', 'Compound',
    'Polymer', 'Resin', 'Latex', 'Rubber', 'Plastic', 'Ceramic', 'Glass',
    'Crystal', 'Mineral', 'Ore', 'Coal', 'Petroleum', 'Gasoline', 'Diesel',
    
    # Abstract forces
    'Gravity', 'Inertia', 'Momentum', 'Friction', 'Pressure', 'Tension',
    'Compression', 'Torsion', 'Stress', 'Strain', 'Force', 'Energy',
    'Power', 'Velocity', 'Acceleration', 'Impact', 'Collision', 'Crash',

    # Sound / music-related
    'Tone', 'Drone', 'Echo', 'Resonance', 'Frequency', 'Vibration',
    'Silence', 'Noise', 'Whisper', 'Chord', 'Harmony', 'Melody',
    'Dissonance', 'Pulse', 'Rhythm', 'Beat', 'Pattern', 'Texture',
    'Timbre', 'Pitch', 'Overtone', 'Feedback', 'Loop', 'Field', 'Recording',

    # Ambient / environmental
    'Forest', 'River', 'Stream', 'Rain', 'Wind', 'Mist', 'Fog', 'Sky',
    'Cloud', 'Sun', 'Moon', 'Star', 'Ocean', 'Wave', 'Shore', 'Cave',
    'Stone', 'Dust', 'Sand', 'Desert', 'Mountain', 'Valley', 'Echo',
    'Light', 'Shadow', 'Reflection', 'Mirage',

    # Surreal / dreamlike
    'Dream', 'Vision', 'Memory', 'Hallucination', 'Illusion', 'Reverie',
    'Nightmare', 'Phantasm', 'Specter', 'Shadow', 'Portal', 'Threshold',
    'Mirror', 'Mask', 'Labyrinth', 'Puzzle', 'Fragment', 'Shape', 'Form',
    'Dimension', 'Sphere', 'Void', 'Aether', 'Continuum', 'Silhouette',

    # Artistic / conceptual
    'Canvas', 'Frame', 'Composition', 'Form', 'Gesture', 'Abstraction',
    'Concept', 'Structure', 'Improvisation', 'Movement', 'Performance',
    'Installation', 'Collage', 'Montage', 'Sequence', 'Cut', 'Shot', 'Scene',
    'Reel', 'Film', 'Projection', 'Screen', 'Light', 'Image', 'Vision',
    'Perception', 'Perspective', 'Frame', 'Focus', 'Exposure',

    # Emotion / state
    'Melancholy', 'Serenity', 'Fear', 'Memory', 'Oblivion', 'Desire',
    'Longing', 'Nostalgia', 'Silence', 'Calm', 'Tension', 'Suspense',
    'Euphoria', 'Dream', 'Rapture', 'Isolation', 'Madness', 'Trance',

    # Abstract / philosophical
    'Existence', 'Essence', 'Void', 'Being', 'Presence', 'Absence',
    'Time', 'Infinity', 'Eternity', 'Moment', 'Cycle', 'Ritual', 'Myth',
    'Symbol', 'Sign', 'Language', 'Noise', 'Order', 'Chaos', 'Form',
    'Perception', 'Consciousness', 'Shadow', 'Light', 'Void',

    # Raw / material
    'Clay', 'Stone', 'Wood', 'Metal', 'Fiber', 'Thread', 'Glass', 'Smoke',
    'Dust', 'Ash', 'Paper', 'Film', 'Celluloid', 'Tape', 'Wire', 'Frame'
]

while True:

    command = input("Press enter to generate 10 usernames ('q' to quit):")
    if command == 'q':
        break
    else:
    
        # Generate 30 username suggestions with no separator
        print("=" * 60)
        print("AVANT-GARDE USERNAME GENERATOR")
        print("=" * 60)
        print()

        for i in range(10):
            username = f"{random.choice(adjectives)}{random.choice(nouns)}"
            print(f"{i+1:2d}. {username}")

        print("\nRun the script again for 30 more combinations!")
        print(f"Total possible combinations: {len(adjectives) * len(nouns):,}\n")
