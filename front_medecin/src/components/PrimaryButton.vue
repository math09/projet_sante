<template>
    <button
      class="w-full py-0.25 bg-gradient-to-r from-emerald-500 to-tropical-rain-forest-700 shadow-xl rounded-md text-x0.5 font-bold text-white"
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