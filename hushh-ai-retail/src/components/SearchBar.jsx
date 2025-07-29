"use client";

import { useState, useRef } from "react";
import {
  TextField,
  Box,
  InputAdornment,
  Paper,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  ClickAwayListener,
} from "@mui/material";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import { Search as SearchIcon } from "@mui/icons-material";
import { suggestions } from "../data";

const SearchBar = ({ onSearch, initialValue = "", showTitle = false }) => {
  const [searchQuery, setSearchQuery] = useState(initialValue);
  const [showSuggestions, setShowSuggestions] = useState(false);

  const inputRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      onSearch(searchQuery.trim());
      setShowSuggestions(false);
    }
  };

  const handleInputFocus = () => {
    if (!searchQuery.trim()) {
      setShowSuggestions(true);
    }
  };

  const handleInputChange = (e) => {
    const value = e.target.value;
    setSearchQuery(value);
    if (value.trim() === "") {
      setShowSuggestions(true);
    } else {
      setShowSuggestions(false);
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setSearchQuery(suggestion);
    setShowSuggestions(false);
    onSearch(suggestion);
  };

  return (
    <ClickAwayListener onClickAway={() => setShowSuggestions(false)}>
      <Box sx={{ width: "100%", maxWidth: 900, position: "relative" }}>
        <form onSubmit={handleSubmit}>
          <Paper
            elevation={2}
            sx={{
              display: "flex",
              alignItems: "center",
              px: 2,
              py: 1,
              borderRadius: "50px",
              boxShadow: 5,
            }}
          >
            <TextField
              fullWidth
              placeholder="Search for products..."
              value={searchQuery}
              onChange={handleInputChange}
              onFocus={handleInputFocus}
              inputRef={inputRef}
              variant="standard"
              InputProps={{
                disableUnderline: true,
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon color="action" />
                  </InputAdornment>
                ),
              }}
              sx={{
                px: 1,
                fontSize: "1.1rem",
              }}
            />
            <IconButton onClick={handleSubmit}>
              <PlayArrowIcon />
            </IconButton>
          </Paper>
        </form>

        {showSuggestions && (
          <Paper
            elevation={3}
            sx={{
              position: "absolute",
              width: "100%",
              mt: 1,
              borderRadius: 2,
              zIndex: 10,
              maxHeight: 200,
              overflowY: "auto",
            }}
          >
            <List>
              {suggestions.map((item, index) => (
                <ListItem key={index} disablePadding>
                  <ListItemButton onClick={() => handleSuggestionClick(item)}>
                    <ListItemText primary={item} />
                  </ListItemButton>
                </ListItem>
              ))}
            </List>
          </Paper>
        )}
      </Box>
    </ClickAwayListener>
  );
};

export default SearchBar;
