<template>
    <div class="flex flex-col">
      <label v-if="label" :for="id" class="mb-2 font-semibold text-md" :class="labelClass">{{ label }}</label>
      <div class="relative flex w-full">
        <div v-if="$slots.default" class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
          <slot></slot>
        </div>
        <input
          :id="id"
          :type="type"
          :placeholder="placeholder"
          :disabled="disabled"
          class="pl-12 pr-5 py-4 text-md border border-gray-50 focus:outline-none focus:border-gray-200 bg-neutral-100 shadow-lg rounded-2xl flex-grow"
          :class="[$slots.default ? 'pl-12' : 'pl-5', inputClass]"
          v-model="model"
          @input="$emit('input-c')"
        />
      </div>
  </div>
</template>

<script setup>
  defineProps({
    id: String,
    type: String,
    placeholder: String,
    disabled: Boolean,
    label: String,
    inputClass: String,
    labelClass: String
  });
  
  const model = defineModel()
</script>