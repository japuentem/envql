import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs("assets_comic", exist_ok=True)

def generate_dev_panic():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    fig.patch.set_facecolor('#0B0F17')
    ax.set_facecolor('#0B0F17')
    
    # Glow behind monitor
    glow = patches.Circle((3, 2.5), 2.2, color='#EF4444', alpha=0.15)
    ax.add_patch(glow)
    
    # Desk
    desk = patches.Rectangle((0.5, 0.5), 5, 0.3, color='#1E293B')
    ax.add_patch(desk)
    
    # Monitor Stand & Screen
    stand = patches.Rectangle((2.8, 0.8), 0.4, 0.6, color='#475569')
    ax.add_patch(stand)
    monitor = patches.Rectangle((1.5, 1.4), 3, 2.2, color='#0F172A', ec='#EF4444', lw=3)
    ax.add_patch(monitor)
    
    # Screen inner red alert
    ax.text(3.0, 2.7, "500 CRITICAL", color='#EF4444', fontsize=18, fontweight='bold', ha='center')
    ax.text(3.0, 2.3, "DATABASE_URLL not found", color='#FCA5A5', fontsize=9, ha='center', fontfamily='monospace')
    ax.text(3.0, 1.9, "Production is DOWN", color='#FFFFFF', fontsize=11, fontweight='bold', ha='center')
    
    # Programmer Face / Panic Cartoon
    head = patches.Circle((4.7, 2.7), 0.65, color='#FDE047', ec='#000000', lw=2)
    ax.add_patch(head)
    
    # Wide scared eyes
    eye1 = patches.Circle((4.5, 2.85), 0.18, color='#FFFFFF', ec='#000000', lw=1.5)
    eye2 = patches.Circle((4.85, 2.85), 0.18, color='#FFFFFF', ec='#000000', lw=1.5)
    pupil1 = patches.Circle((4.5, 2.85), 0.05, color='#000000')
    pupil2 = patches.Circle((4.85, 2.85), 0.05, color='#000000')
    ax.add_patch(eye1); ax.add_patch(eye2); ax.add_patch(pupil1); ax.add_patch(pupil2)
    
    # Screaming mouth
    mouth = patches.Ellipse((4.68, 2.45), 0.35, 0.35, color='#991B1B', ec='#000000', lw=2)
    ax.add_patch(mouth)
    
    # Sweat drops
    sweat = patches.Polygon([[4.15, 3.1], [4.1, 3.25], [4.2, 3.25]], color='#38BDF8')
    ax.add_patch(sweat)
    
    # Hands on head
    hand1 = patches.Circle((4.1, 3.1), 0.2, color='#FACC15', ec='#000000', lw=1.5)
    hand2 = patches.Circle((5.25, 3.1), 0.2, color='#FACC15', ec='#000000', lw=1.5)
    ax.add_patch(hand1); ax.add_patch(hand2)
    
    # Coffee mug on desk
    mug = patches.Rectangle((0.8, 0.8), 0.5, 0.6, color='#3B82F6', ec='#1D4ED8', lw=1.5)
    ax.add_patch(mug)
    ax.text(1.05, 1.0, "2 AM", color='#FFFFFF', fontsize=7, fontweight='bold', ha='center')
    
    # Speech bubble
    bubble = patches.FancyBboxPatch((1.0, 3.8), 3.2, 0.9, boxstyle="round,pad=0.2", fc="#FFFFFF", ec="#000000", lw=2)
    ax.add_patch(bubble)
    ax.text(2.6, 4.4, "¡¿Quien escribio", color='#000000', fontsize=12, fontweight='bold', ha='center')
    ax.text(2.6, 4.05, "DATABASE_URLL con doble L?!", color='#DC2626', fontsize=12, fontweight='bold', ha='center')
    
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig("assets_comic/dev_panic.png", facecolor='#0B0F17', bbox_inches='tight')
    plt.close()
    print("dev_panic.png generated")

def generate_shield_hero():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    fig.patch.set_facecolor('#0B0F17')
    ax.set_facecolor('#0B0F17')
    
    # Blue shield
    shield_pts = np.array([
        [3.0, 4.5], [4.5, 4.0], [4.4, 2.0], [3.0, 0.8], [1.6, 2.0], [1.5, 4.0]
    ])
    shield = patches.Polygon(shield_pts, color='#0284C7', ec='#38BDF8', lw=4)
    ax.add_patch(shield)
    
    # Inner shield accent
    inner_shield_pts = np.array([
        [3.0, 4.2], [4.2, 3.8], [4.1, 2.2], [3.0, 1.2], [1.9, 2.2], [1.8, 3.8]
    ])
    inner_shield = patches.Polygon(inner_shield_pts, color='#0369A1')
    ax.add_patch(inner_shield)
    
    # Lock or Checkmark
    ax.text(3.0, 2.7, "EnvQL", color='#FFFFFF', fontsize=24, fontweight='bold', ha='center')
    ax.text(3.0, 2.0, "AES-256", color='#38BDF8', fontsize=14, fontweight='bold', ha='center')
    ax.text(3.0, 1.5, "FAIL-FAST", color='#4ADE80', fontsize=12, fontweight='bold', ha='center')
    
    # Comic stars / sparkles
    ax.text(0.8, 4.2, "✨", fontsize=24)
    ax.text(4.8, 4.2, "⚡", fontsize=24)
    ax.text(0.6, 1.8, "🛡️", fontsize=24)
    ax.text(4.8, 1.5, "🔒", fontsize=24)
    
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig("assets_comic/shield_hero.png", facecolor='#0B0F17', bbox_inches='tight')
    plt.close()
    print("shield_hero.png generated")

if __name__ == "__main__":
    generate_dev_panic()
    generate_shield_hero()
