<template>
    <section class="about-us-section bg-[var(--accent-offwhite)] py-16 px-4">
      <div class="container mx-auto flex flex-col md:flex-row items-center">
        <!-- Image -->
        <div class="md:w-1/2 mb-8 md:mb-0 md:pr-8">
          <img :src="aboutUsImage" alt="Elegant Restaurant Interior" class="rounded-lg shadow-lg">
        </div>
        <!-- Text Content -->
        <div class="md:w-1/2 text-center md:text-left">
          <h2 class="text-4xl font-bold text-[var(--primary-gold)] mb-4" style="font-family: var(--font-title);">
            About Us
          </h2>
          <p class="text-xl text-[var(--darker-charcoal)] leading-relaxed" style="font-family: var(--font-button);">
            Established in 2010, 
            <span class="font-black text-[var(--primary-gold)]" style="font-family: var(--font-body);">Noir et Or</span> 
            began with a vision to bring the essence of fine Italian dining to the heart of the city. Our name, translating to "Black and Gold," symbolizes the elegance and opulence that define our dining experience. Over the years, we have expanded to three prestigious locations, each upholding the same sophistication and culinary excellence.
            <br /><br />
            At 
            <span class="font-black text-[var(--primary-gold)]" style="font-family: var(--font-body);">Noir et Or</span>, 
            we believe in crafting more than just meals; we create unforgettable experiences. Our team of passionate chefs and attentive staff is dedicated to ensuring that every visit is a journey of taste, comfort, and style. From meticulously sourced ingredients to expertly curated dishes, we take pride in delivering perfection.
            <br /><br />
            Join us and indulge in a luxurious atmosphere where tradition meets modern culinary artistry. Welcome to 
            <span class="font-black text-[var(--primary-gold)]" style="font-family: var(--font-body);">Noir et Or</span>, 
            where every moment is a celebration of elegance and flavor.
          </p>
        </div>
      </div>
    </section>
</template>

<script setup>
import aboutUsImage from '@/assets/about-image.jpg';
</script>
