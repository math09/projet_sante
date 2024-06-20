<template>
    <button
      class="px-20 py-3 bg-gradient-to-r from-teal-500 to-teal-300 shadow-xl rounded-2xl text-xl font-bold text-white"
      :class="buttonClass"
      :disabled="disabled"
    >
      <slot></slot>
    </button>
</template>
  
<script>
  export default {
    name: 'PrimaryButton',
    props: {
      buttonClass: {
        type: String,
        default: ''
      },
      disabled: {
        type: Boolean,
        default: false
      }
    }
  };
</script>