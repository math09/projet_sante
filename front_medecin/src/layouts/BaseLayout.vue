<template>
  <main>
    <div class=" absolute w-[200%] h-[100%] -left-1/2 top-[30%] bg-gradient-to-r from-emerald-500 to-tropical-rain-forest-700 rounded-[50%] -z-10"></div>
    <img src="../assets/icon.png" class="fixed w-24 top-2 left-2">
    <div class="w-screen h-screen px-20 py-16">
      <div class="w-full h-full p-6 shadow-2xl bg-neutral-100 rounded-2xl">
        <slot></slot>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'BaseLayout'
};
</script>