"use client";

import { useState, useEffect, useRef } from "react";
import { useSearchParams, useNavigate, useLocation } from "react-router-dom";
import {
  Container,
  Box,
  Typography,
  CircularProgress,
  Alert,
  Accordion,
  AccordionSummary,
  AccordionDetails,
} from "@mui/material";
import ReactMarkdown from "react-markdown";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";
import SearchBar from "./SearchBar";
import { getDeals } from "../services";
import hushhLogo from "../assets/hushh_new_logo.svg";

const ResultsPage = () => {
  const location = useLocation();
  const selectedEmail = location.state?.selectedEmail;
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const streaminglogsContainerRef = useRef(null);
  const [results, setResults] = useState(null);
  const [streamingLogs, setStreamingLogs] = useState([]);
  const [showLogs, setShowLogs] = useState(true);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const query = searchParams.get("q") || "";

  const fetchResults = async (searchQuery) => {
    setLoading(true);
    setError(null);
    setStreamingLogs([]);
    setShowLogs(true);

    try {
      const payload = {
        user_email: selectedEmail,
        instruction: query,
      };

      const onStreamMessage = (msg) => {
        setStreamingLogs((prev) => [...prev, msg]);
      };

      const onFinalReport = (result) => {
        setResults(result);
        setShowLogs(false);
      };

      await getDeals(payload, onStreamMessage, onFinalReport);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };


  useEffect(() => {
    if (query) {
      fetchResults(query);
    }
  }, [query]);

  useEffect(() => {
    if (streaminglogsContainerRef.current) {
      streaminglogsContainerRef.current.scrollTop =
        streaminglogsContainerRef.current.scrollHeight;
    }
  }, [streamingLogs]);

  const handleNewSearch = (newQuery) => {
    navigate(`/results?q=${encodeURIComponent(newQuery)}`);
  };

  if (!query) {
    navigate("/");
    return null;
  }

  return (
    <Container maxWidth="lg">
      <Box sx={{ py: 3 }}>
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            mb: 4,
          }}
        >
          <img
            src={hushhLogo}
            alt="Logo"
            style={{ height: 90, marginBottom: 12 }}
          />
          <SearchBar onSearch={handleNewSearch} initialValue={query} />
        </Box>

        {/* Results section */}
        <Box sx={{ mt: 4 }}>
          {/* {loading && (
            <Box sx={{ display: "flex", justifyContent: "center", py: 4 }}>
              <CircularProgress size={60} thickness={6} sx={{ mr: 2 }}/>
              <p>Hushh AI is retrieving results for you...</p>
            </Box>
          )} */}

          {/* <button
            onClick={() => setShowLogs((prev) => !prev)}
            style={{
              padding: "6px 12px",
              backgroundColor: "#1976d2",
              color: "white",
              border: "none",
              borderRadius: 4,
              cursor: "pointer",
            }}
          >
            {showLogs ? "Hide Logs" : "Show Logs"}
          </button> */}

          {/* {loading && (
            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                py: 4,
              }}
            >
              <CircularProgress size={60} thickness={6} sx={{ mb: 2 }} /> */}

          {/* {streamingLogs.length > 0 && ( */}
          <Accordion
            sx={{
              mt: 2,
              width: "100%",
              borderRadius: 5,
              boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
            }}
            expanded={showLogs}
            onChange={() => setShowLogs((prev) => !prev)}
          >
            <AccordionSummary expandIcon={null}>
              <Box sx={{ display: "flex", alignItems: "center" }}>
                {loading && (
                  <CircularProgress size={20} thickness={4} sx={{ mr: 1 }} />
                )}
                {showLogs ? <ExpandLessIcon /> : <ExpandMoreIcon />}
                <Typography variant="subtitle1" sx={{ ml: 1 }}>
                  {showLogs ? "Hide Thinking" : "Show Thinking"}
                </Typography>
              </Box>
            </AccordionSummary>
            <AccordionDetails>
              <Box
                // className="markdown"
                ref={streaminglogsContainerRef}
                sx={{
                  bgcolor: "#eeeeee",
                  fontFamily: "monospace",
                  maxHeight: 300,
                  overflowY: "auto",
                  borderRadius: 5,
                  whiteSpace: "pre-wrap",
                  p: 2,
                }}
              >
                {streamingLogs ? (
                  streamingLogs.map((line, idx) => {
                    const cleanLine = line
                      .trim()
                      // .replace(/\t/g, "")
                      // .replace(/^>\s?/gm, "");
                    return <ReactMarkdown key={idx}>{cleanLine}</ReactMarkdown>;
                  })
                ) : (
                  <Typography
                    variant="body2"
                    sx={{ fontStyle: "italic", opacity: 0.6 }}
                  >
                    ...
                  </Typography>
                )}
              </Box>
            </AccordionDetails>
          </Accordion>
          {/* )} */}
          {/* </Box>
          )} */}

          {error && (
            <Alert severity="error" sx={{ mb: 3 }}>
              {error}
            </Alert>
          )}

          {results && !loading && (
            <>
              <Box
                sx={{
                  mb: 3,
                  mt: 2,
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  flexWrap: "wrap", // allows wrapping when needed
                }}
              >
                <ReactMarkdown>{results}</ReactMarkdown>;

                {/* <Paper
                  sx={{
                    px: 2,
                    py: 1,
                    borderRadius: 20,
                    bgcolor: "#444444",
                    flexShrink: 0, // prevents shrinking
                    mt: { xs: 2, sm: 0 }, // adds top margin on small screens if it wraps
                  }}
                >
                  <Typography
                    variant="body2"
                    color="#fff"
                    sx={{ fontWeight: 700, fontSize: "1rem" }}
                  >
                    True Price: ₹{results.true_price}
                  </Typography>
                </Paper> */}
              </Box>

              {/* <Typography
                variant="body2"
                color="text.secondary"
                sx={{ mb: 3, fontSize: "1.2rem" }}
              >
                Found {results.mall_resp.length} results
              </Typography> */}

              {/* {results.mall_resp.map((item, index) => (
                <ResultCard
                  key={index}
                  shop_name={item.shop_name}
                  product={item.product}
                  discount={item.discount}
                  personalized_offer={item.personalized_offer}
                  offer_price={item.offer_price}
                  true_price={item.true_price}
                />
              ))} */}
            </>
          )}
        </Box>
      </Box>
    </Container>
  );
};

export default ResultsPage;
