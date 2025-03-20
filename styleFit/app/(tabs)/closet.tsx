import React, { useState } from "react";
import {
  View,
  Text,
  ScrollView,
  Image,
  TouchableOpacity,
  Modal,
  Alert,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { MaterialIcons } from "@expo/vector-icons";
import { useTheme } from "../../components/ThemeContext";
import * as ImagePicker from "expo-image-picker";

const DUMMY_ITEMS = [
  { id: "1", type: "Shirt", image: "https://via.placeholder.com/150" },
  { id: "2", type: "Pants", image: "https://via.placeholder.com/150" },
  { id: "3", type: "Dress", image: "https://via.placeholder.com/150" },
  { id: "4", type: "Shoes", image: "https://via.placeholder.com/150" },
];

export default function ClosetScreen() {
  const { isDarkMode } = useTheme();
  const [isModalVisible, setIsModalVisible] = useState(false);

  const requestPermissions = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== "granted") {
      Alert.alert(
        "Permission needed",
        "Please grant camera roll permissions to add photos."
      );
      return false;
    }
    return true;
  };

  const takePicture = async () => {
    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== "granted") {
      Alert.alert(
        "Permission needed",
        "Please grant camera permissions to take photos."
      );
      return;
    }

    const result = await ImagePicker.launchCameraAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 0.8,
    });

    if (!result.canceled) {
      // Handle the captured image
      console.log(result.assets[0].uri);
      // Add your logic to save the image
    }
    setIsModalVisible(false);
  };

  const pickImage = async () => {
    if (!(await requestPermissions())) return;

    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 0.8,
    });

    if (!result.canceled) {
      // Handle the selected image
      console.log(result.assets[0].uri);
      // Add your logic to save the image
    }
    setIsModalVisible(false);
  };

  return (
    <SafeAreaView
      className={`flex-1 ${isDarkMode ? "bg-gray-900" : "bg-white"}`}
    >
      <View className="px-4 py-2">
        <View className="flex-row justify-between items-center mb-4">
          <Text
            className={`text-xl font-semibold ${
              isDarkMode ? "text-gray-100" : "text-gray-800"
            }`}
          >
            My Closet
          </Text>
          <TouchableOpacity
            className="bg-indigo-500 rounded-full p-2"
            onPress={() => setIsModalVisible(true)}
          >
            <MaterialIcons name="add" size={24} color="white" />
          </TouchableOpacity>
        </View>

        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          className="mb-4"
        >
          {["All", "Tops", "Bottoms", "Dresses", "Shoes", "Accessories"].map(
            (category) => (
              <TouchableOpacity
                key={category}
                className={`mr-2 px-4 py-2 rounded-full ${
                  isDarkMode ? "bg-gray-800" : "bg-gray-100"
                }`}
              >
                <Text
                  className={isDarkMode ? "text-gray-100" : "text-gray-800"}
                >
                  {category}
                </Text>
              </TouchableOpacity>
            )
          )}
        </ScrollView>
      </View>

      <ScrollView className="flex-1 px-4">
        <View className="flex-row flex-wrap justify-between">
          {DUMMY_ITEMS.map((item) => (
            <TouchableOpacity
              key={item.id}
              className={`w-[48%] rounded-lg mb-4 overflow-hidden ${
                isDarkMode ? "bg-gray-800" : "bg-gray-50"
              }`}
            >
              <Image
                source={{ uri: item.image }}
                className="w-full h-48"
                resizeMode="cover"
              />
              <View className="p-2">
                <Text
                  className={isDarkMode ? "text-gray-100" : "text-gray-800"}
                >
                  {item.type}
                </Text>
              </View>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>

      {/* Image Source Modal */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={isModalVisible}
        onRequestClose={() => setIsModalVisible(false)}
      >
        <TouchableOpacity
          className="flex-1 justify-end bg-black/50"
          onPress={() => setIsModalVisible(false)}
        >
          <View
            className={`${
              isDarkMode ? "bg-gray-800" : "bg-white"
            } rounded-t-3xl p-4`}
          >
            <View className="items-center mb-6">
              <View className="w-16 h-1 bg-gray-300 rounded-full mb-4" />
              <Text
                className={`text-lg font-semibold ${
                  isDarkMode ? "text-white" : "text-gray-800"
                }`}
              >
                Add Photo
              </Text>
            </View>

            <TouchableOpacity
              className="flex-row items-center p-4 mb-2"
              onPress={takePicture}
            >
              <MaterialIcons
                name="camera-alt"
                size={24}
                color={isDarkMode ? "#fff" : "#4B5563"}
              />
              <Text
                className={`ml-4 text-lg ${
                  isDarkMode ? "text-white" : "text-gray-600"
                }`}
              >
                Take Photo
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              className="flex-row items-center p-4 mb-4"
              onPress={pickImage}
            >
              <MaterialIcons
                name="photo-library"
                size={24}
                color={isDarkMode ? "#fff" : "#4B5563"}
              />
              <Text
                className={`ml-4 text-lg ${
                  isDarkMode ? "text-white" : "text-gray-600"
                }`}
              >
                Choose from Library
              </Text>
            </TouchableOpacity>
          </View>
        </TouchableOpacity>
      </Modal>
    </SafeAreaView>
  );
}
