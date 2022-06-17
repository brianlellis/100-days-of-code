import React from 'react'
import { Button, Text, StyleSheet, View, Image } from 'react-native'

const strRGB = (name, rgb) => {
  if (name == 'Red')        return `rgb(${rgb},0,0)`
  else if (name == 'Green') return `rgb(0,${rgb},0)`
  else if (name == 'Blue')  return `rgb(0,0,${rgb})`
  return 'rgb(0,0,0)'
}
const ColorChanger = ({name, rgb, onIncrease, onDecrease}) => (
  <View>
    <Button onPress={() => onIncrease()} title={`Increase ${name}`} />
    <Button onPress={() => onDecrease()} title={`Decrease ${name}`} />
    <View style={{height:100, width: 100, backgroundColor: strRGB(name, rgb) }}></View>
  </View>
)

export default ColorChanger