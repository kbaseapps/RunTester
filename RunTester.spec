/*
A KBase module: RunTester
*/

module RunTester {
    typedef structure {
        string report_name;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_RunTester(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
