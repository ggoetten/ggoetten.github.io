import os

# Helper dictionaries to keep descriptions consistent and high-level
course_info = {
    "AP Physics C: Electricity and Magnetism": {
        "summary": "Calculus-based course on electrostatics, circuits, and electromagnetism.",
        "tags": ["Physics", "AP", "Electromagnetism", "Calculus-Based"],
        "content": "A comprehensive 40-hour course covering the full AP Physics C: Electricity and Magnetism curriculum. Topics include electrostatics, conductors, capacitors, electric circuits, magnetic fields, and electromagnetism."
    },
    "AP Physics C: Mechanics": {
        "summary": "Calculus-based course covering kinematics, dynamics, and rotation.",
        "tags": ["Physics", "AP", "Mechanics", "Calculus-Based"],
        "content": "A comprehensive 40-hour course covering the full AP Physics C: Mechanics curriculum. Key topics include kinematics, Newton's laws of motion, work, energy, power, linear momentum, and rotational dynamics."
    },
    "AP Physics 1": {
        "summary": "Algebra-based foundational physics course covering mechanics and fluids.",
        "tags": ["Physics", "AP", "Algebra-Based"],
        "content": "A comprehensive 40-hour algebra-based physics course. The curriculum covers systems, fields, force interactions, change, conservation laws, and fluid dynamics."
    },
    "New Teacher Training": {
        "summary": "Professional development for remote instruction pedagogy.",
        "tags": ["Pedagogy", "Training"],
        "content": "Professional training session focused on instructional design, digital classroom management, and student engagement strategies."
    }
}

# Specific session data from your list
sessions = [
    {"date": "2026-02-07", "title": "AP Physics C: Electricity and Magnetism", "role": "Teacher"},
    {"date": "2026-01-19", "title": "AP Physics C: Electricity and Magnetism", "role": "Teacher"},
    {"date": "2025-12-06", "title": "AP Physics C: Electricity and Magnetism", "role": "Teacher"},
    {"date": "2025-11-10", "title": "AP Physics 1", "role": "Teacher"},
    {"date": "2025-10-23", "title": "AP Physics 1", "role": "Teacher"},
    {"date": "2025-09-29", "title": "AP Physics 1", "role": "Teacher"},
    {"date": "2025-09-05", "title": "AP Physics C: Electricity and Magnetism", "role": "Teacher"},
    {"date": "2025-07-19", "title": "AP Physics C: Mechanics", "role": "Teacher"},
    {"date": "2025-06-10", "title": "AP Physics 1", "role": "Teacher"},
    {"date": "2025-03-04", "title": "AP Physics 1", "role": "Teacher"},
    {"date": "2025-01-10", "title": "New Teacher Training", "role": "Student"}, # Kept approximate date
]

def generate_teaching_data():
    teaching_data = []
    for session in sessions:
        # Get generic info based on title (handle partial matches if needed, but exact here)
        base_title = session["title"].replace(": Algebra-Based", "") # Normalize title lookup if needed
        
        # Fallback for exact lookup
        info = course_info.get(session["title"], course_info.get(base_title, {}))
        
        if not info:
             # Fallback default
            info = {
                "summary": "Physics instruction session.",
                "tags": ["Physics"],
                "content": "Instructional session."
            }

        filename = f"{session['title'].replace(':', '').replace(' ', '-').lower()}-{session['date']}.md"
        
        entry = {
            "filename": filename,
            "title": session["title"],
            "date": session["date"],
            "role": session["role"],
            "location": "American Straight A Academy" if session["role"] == "Teacher" else "Professional Development",
            "summary": info["summary"],
            "tags": info["tags"],
            "content": info["content"]
        }
        teaching_data.append(entry)
    return teaching_data

def generate_markdown(item):
    """Formats the front matter and content for the MD file."""
    # Convert list of tags to string representation
    tags_str = str(item['tags']).replace("'", '"')
    
    front_matter = f"""---
title: "{item['title']}"
date: {item['date']}
publishdate: {item['date']}
role: "{item['role']}"
location: "{item['location']}"
summary: "{item['summary']}"
tags: {tags_str}
---

{item['content']}
"""
    return front_matter

def main():
    target_dir = "content/teaching"
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created directory: {target_dir}")

    data = generate_teaching_data()

    for item in data:
        file_path = os.path.join(target_dir, item['filename'])
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generate_markdown(item))
        print(f"Generated: {file_path}")

    print("\nAll teaching files have been generated successfully.")

if __name__ == "__main__":
    main()