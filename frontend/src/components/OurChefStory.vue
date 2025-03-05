<template>
  <section class="py-16 bg-[var(--bg-deep-burgundy-light)] text-[var(--text-white)] text-center">
    <div class="container mx-auto">
      <!-- Section Title -->
      <h2 class="text-4xl font-bold mb-8 text-[var(--primary-gold)]" style="font-family: var(--font-title);">
        Our Chef's Story
      </h2>
      <!-- Chef Image -->
      <div class="relative mx-auto w-56 h-56 rounded-full overflow-hidden border-4 border-[var(--primary-gold)]">
        <img 
          :src="chefImage" 
          alt="Chef Alessandro Rossi" 
          class="w-full h-full object-cover object-top scale-[1.0]"
        />
      </div>
      <!-- Chef's Story -->
      <p class="mt-6 text-lg leading-relaxed" style="font-family: var(--font-button);">
        Meet <span class="text-[var(--primary-gold)] font-bold">Chef Alessandro Rossi</span>, the culinary mastermind behind Noir et Or.
        With over two decades of experience in Michelin-starred restaurants across Europe, Chef Rossi brings a wealth of knowledge and passion to our kitchen.
        Raised in the picturesque hills of Tuscany, Chef Rossi grew up surrounded by the rich culinary traditions of Italy. Inspired by his family's love for
        food and wine, he developed an early appreciation for authentic flavors and artisanal techniques.
        Driven by his passion, he pursued his culinary education at the prestigious Culinary Institute of Florence. Under the mentorship of world-renowned chefs,
        he honed his craft and mastered the art of blending traditional Italian cuisine with modern influences.
        <br /><br />
        <span class="text-[var(--primary-gold)] font-bold">Chef Rossi's Philosophy:</span> 
        At Noir et Or, Chef Rossi believes in celebrating the integrity of each ingredient. He carefully sources the finest seasonal produce, ensuring that each dish
        reflects the vibrant essence of Italy. His culinary creations are a harmonious balance of tradition and innovation, designed to delight the senses. 
        Chef Rossi approaches his dishes with the philosophy that simplicity and authenticity create the most profound experiences. 
        His menu is crafted to evoke memories of Italy’s rich culinary heritage while introducing a modern flair that excites the palate. 
        Every plate tells a story, meticulously plated to be as visually captivating as it is delicious.
        <br /><br />
        Join us and experience Chef Alessandro Rossi's culinary artistry, where every dish tells a story of heritage, passion, and excellence.
      </p>
    </div>
  </section>
</template>

<script setup>
import chefImage from '@/assets/chef-story.jpg';
</script>
