<template>
    <button
      class="w-full bg-gradient-to-r from-emerald-500 to-tropical-rain-forest-700 shadow-xl rounded-md text-x0.5 font-bold"
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