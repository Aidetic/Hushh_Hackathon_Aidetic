import { useNavigate } from "react-router-dom";
import {
  Container,
  Box,
  Typography,
  Tooltip,
  IconButton,
  Menu,
  MenuItem,
} from "@mui/material";
import SearchBar from "./SearchBar";
import { staticEmails, welcomeText } from "../data/static";
import hushhLogo from "../assets/hushh_new_logo.svg";
import { useState } from "react";
// import { MoreVert } from "@mui/icons-material";
import PersonIcon from "@mui/icons-material/Person";

const SearchPage = () => {
  const navigate = useNavigate();
  const [selectedEmail, setSelectedEmail] = useState("pandeygag78934@gmail.com");
  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleSearch = (query) => {
    navigate(`/results?q=${encodeURIComponent(query)}`, {
      state: { selectedEmail },
    });
  };
  return (
    <Container maxWidth={false} disableGutters>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
          mt: 2,
          mr: 2,
        }}
      >
        <Tooltip title={selectedEmail || "Select user"}>
          <IconButton
            onClick={handleClick}
            size="large"
            aria-controls={open ? "dropdown-menu" : undefined}
            aria-haspopup="true"
            aria-expanded={open ? "true" : undefined}
          >
            <PersonIcon />
          </IconButton>
        </Tooltip>
        <Menu
          id="dropdown-menu"
          anchorEl={anchorEl}
          open={open}
          onClose={handleClose}
          anchorOrigin={{
            vertical: "bottom",
            horizontal: "right",
          }}
          transformOrigin={{
            vertical: "top",
            horizontal: "right",
          }}
        >
          {staticEmails.map((email, index) => (
            <MenuItem
              key={index}
              selected={email === selectedEmail}
              onClick={() => {
                setSelectedEmail(email); // set the selected name
                setAnchorEl(null); // close menu
              }}
            >
              {email}
            </MenuItem>
          ))}
        </Menu>
      </Box>

      <Box
        sx={{
          minHeight: "80vh",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          py: 6,
          width: "100%",
        }}
      >
        <Box sx={{ textAlign: "center", mb: 3 }}>
          <Box sx={{ mb: 2 }}>
            <img src={hushhLogo} alt="Logo" style={{ height: 120 }} />
          </Box>
          <Typography
            variant="h2"
            fontWeight="bold"
            fontSize="2rem"
            color="primary"
          >
            {welcomeText}
          </Typography>
        </Box>
        <SearchBar onSearch={handleSearch} showTitle={true} />
      </Box>
    </Container>
  );
};

export default SearchPage;
