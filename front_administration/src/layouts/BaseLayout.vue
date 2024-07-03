<template>
  <main>
    <div class=" absolute w-[200%] h-[100%] -left-1/2 top-[30%] bg-gradient-to-r from-teal-500 to-teal-300 rounded-[50%] -z-10"></div>
    <img src="../assets/icon.png" class=" w-24 fixed top-2 left-2">
    <div class="w-screen h-screen px-24 py-20">
      <div class="bg-neutral-100 w-full h-full p-8 rounded-2xl shadow-2xl">
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