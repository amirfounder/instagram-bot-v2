export const handleSeedHashtagInputChangeService = (value, setValue) => {
  let newValue = value;
  
  if (newValue !== '') {
    newValue = newValue.startsWith('#') ? newValue : '#' + newValue;
    newValue = newValue.toLowerCase();
    newValue = newValue.trim();
  }

  setValue(newValue)
}

export const handleBotAccountInputChangeService = (value, setValue) => {
  let newValue = value;
  
  if (newValue !== '') {
    newValue = newValue.startsWith('@') ? newValue : '@' + newValue;
    newValue = newValue.toLowerCase();
    newValue = newValue.trim();
  }

  setValue(newValue)
}
