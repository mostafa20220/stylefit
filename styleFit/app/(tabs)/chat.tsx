import React, { useState } from "react";
import {
  View,
  TextInput,
  FlatList,
  Text,
  TouchableOpacity,
  KeyboardAvoidingView,
  Platform,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { useTheme } from "../../components/ThemeContext";
import { MaterialIcons } from "@expo/vector-icons";

interface Message {
  id: string;
  text: string;
  isUser: boolean;
}

export default function ChatScreen() {
  const { isDarkMode } = useTheme();
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState("");

  const sendMessage = () => {
    if (inputText.trim() === "") return;

    const newMessage: Message = {
      id: Date.now().toString(),
      text: inputText,
      isUser: true,
    };

    setMessages([...messages, newMessage]);
    setInputText("");

    // Simulate AI response
    setTimeout(() => {
      const aiResponse: Message = {
        id: (Date.now() + 1).toString(),
        text: "Thanks for your message! I'm here to help with your style needs.",
        isUser: false,
      };
      setMessages((prev) => [...prev, aiResponse]);
    }, 1000);
  };

  const renderMessage = ({ item }: { item: Message }) => (
    <View
      className={`mx-4 my-2 p-3 rounded-lg max-w-[80%] ${
        item.isUser
          ? "bg-indigo-500 self-end"
          : isDarkMode
          ? "bg-gray-700 self-start"
          : "bg-gray-200 self-start"
      }`}
    >
      <Text
        className={`${
          item.isUser || isDarkMode ? "text-white" : "text-gray-800"
        }`}
      >
        {item.text}
      </Text>
    </View>
  );

  return (
    <SafeAreaView
      className={`flex-1 ${isDarkMode ? "bg-gray-900" : "bg-white"}`}
    >
      <KeyboardAvoidingView
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        className="flex-1"
      >
        <FlatList
          data={messages}
          renderItem={renderMessage}
          keyExtractor={(item) => item.id}
          contentContainerStyle={{ flexGrow: 1 }}
          className="flex-1"
        />
        <View
          className={`flex-row items-center p-4 border-t ${
            isDarkMode ? "border-gray-700" : "border-gray-200"
          }`}
        >
          <TextInput
            className={`flex-1 rounded-full px-4 py-2 mr-2 ${
              isDarkMode
                ? "bg-gray-800 text-white"
                : "bg-gray-100 text-gray-900"
            }`}
            value={inputText}
            onChangeText={setInputText}
            placeholder="Type a message..."
            placeholderTextColor={isDarkMode ? "#9ca3af" : "#6b7280"}
            multiline
          />
          <TouchableOpacity
            onPress={sendMessage}
            className="bg-indigo-500 rounded-full p-2 w-10 h-10 items-center justify-center"
          >
            <MaterialIcons name="send" size={20} color="white" />
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}
