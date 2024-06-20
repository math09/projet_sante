<template>
    <div class="flex flex-col">
      <label v-if="label" :for="id" class="mb-2 font-semibold text-md" :class="labelClass">{{ label }}</label>
      <input
        :id="id"
        :type="type"
        :placeholder="placeholder"
        :disabled="disabled"
        class="px-5 py-4 text-md border border-gray-50 focus:outline-none focus:border-gray-200 bg-neutral-100 shadow-lg rounded-2xl"
        :class="inputClass"
        v-model="model"
      />
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