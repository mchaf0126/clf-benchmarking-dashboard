from pathlib import Path
import pandas as pd
from dash import html, dcc, register_page, Input, Output, callback
import dash_bootstrap_components as dbc
from src.components.jumbotron import create_jumbotron


register_page(__name__, path='/')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]
metadata_directory = main_directory.joinpath('data/buildings_metadata.pkl')
buildings_metadata_df = pd.read_pickle(metadata_directory)

typology_jumbotron = create_jumbotron(
    subtitle='Unique Building Typologies',
    main_text=len(buildings_metadata_df['bldg_prim_use'].unique()),
)

project_number_jumbotron = create_jumbotron(
    subtitle='Projects in Dataset',
    main_text=buildings_metadata_df.shape[0]
)

avg_impact_jumbotron = create_jumbotron(
    subtitle='Average kgCO2e / m2',
    main_text=round(buildings_metadata_df['eci_a_to_c_gfa'].mean())
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            '''
                            #### About this study
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            In 2017, the Carbon Leadership Forum (CLF) at the 
                            University of Washington published the **[Embodied 
                            Carbon Benchmark Study V1]
                            (https://carbonleadershipforum.org/lca-benchmark-database/)**
                            and **[Visualization Tool]
                            (https://carbonleadershipforum.org/embodied-carbon-benchmark-study-data-visualization/)**. 
                            Since then, the practice of whole-building life 
                            cycle assessment (WBLCA) has grown rapidly, and 
                            it became clear that more robust and reliable 
                            benchmarks are critical for advancing work in this
                            field. This project fills a critical gap and helps 
                            enable architects, engineers, policy makers, and 
                            the entire design community to work towards 
                            realistic and measurable embodied carbon reductions
                            at the building scale.
                            
                            The **[WBLCA Benchmark Study V2]
                            (https://carbonleadershipforum.org/clf-wblca-v2/)**
                            began while the Carbon Leadership Forum (CLF) 
                            was hosted at the University 
                            of Washington (UW). After the CLF became an 
                            independent nonprofit in the spring of 2024, the 
                            study continued as a collaboration between the UW’s 
                            newly named Life Cycle Lab and CLF.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### About the dashboard
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            There are
                            currently two types of graphs available:
                            *  **[Box plot](/box_plot)** - the traditional benchmarking graph. 
                            This plot shows environmental impacts based on categorical 
                            variables (e.g. building use, number of stories or 
                            location). All environmental impacts are inclusive
                            of life cycle stages A-C.
                            *  **[Scatter plot](/scatter_plot)** - good for analyzing relationships.
                            This plot shows environmental impacts compared to continuous
                            variables (e.g. floor area, window-to-wall ratio or 
                            column spacing). All environmental impacts are inclusive
                            of life cycle stages A-C.
                            
                            Please refer to the Data Glossary in the **[WBLCA Benchmark v2 Data 
                            Github Repository](https://github.com/Life-Cycle-Lab/wblca-benchmark-v2-data)**
                            for any questions related to categorical or continuous variable definitions.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### Useful Links
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            - **[Study Landing Page]
                            (https://carbonleadershipforum.org/clf-wblca-v2/)**
                            - **[California Carbon Report]
                            (https://carbonleadershipforum.org/california-carbon/)**
                            - **[Dataset hosted on Figshare]
                            (https://doi.org/10.6084/m9.figshare.28462145.v1)**
                            - **[Data Descriptor Paper (preprint)]
                            (https://doi.org/10.21203/rs.3.rs-6108016/v1)**
                            - **[Material Use Intensity Paper (preprint)]
                            (https://doi.org/10.21203/rs.3.rs-6315460/v1)**
                            - **[Data Collection User Guide]
                            (https://hdl.handle.net/1773/51285)**
                            - **[Data Entry Template]
                            (https://hdl.handle.net/1773/51286)**
                            - **[Github Repository for Dashboard]
                            (https://github.com/Life-Cycle-Lab/wblca-benchmark-v2-dashboard)**
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### About the University of Washington (UW) Life Cycle Lab
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            The **[Life Cycle Lab](https://www.lifecyclelab.org/)**
                            at UW’s College of Built Environments leads
                            research to advance life cycle assessment (LCA) data, methods,
                            and approaches to enable the optimization of materials, buildings,
                            and infrastructure. Our work is structured to inform impactful
                            policies and practices that support global decarbonization efforts.
                            We envision a transformed, decarbonized building
                            industry – better buildings for a better planet.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### Authors
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            The individuals from the Carbon Leadership Forum who worked on this
                            dashboard are:
                            - Manuel Chafart, Reseacher (now at Carbon Leadership Forum)
                            - Brad Benke, Researcher (now at Carbon Leadership Forum)
                            - Kathrina Simonen, Professor

                            **[CRediT]
                            (https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement)**
                            authorship contribution: Conceptualization - B.B., M.C.,
                            Formal analysis: M.C; Methodology - B.B., M.C.;  Visualization: M.C;
                            Supervision and Funding Acquisition: K.S.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### Acknowledgements
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            We would like to thank the individuals and respective firms
                            who participated in the data collection and quality assurance
                            process, this work would not have been possible without their
                            incredible support and dedication to thisproject. These
                            included: Arrowstreet Architects, Arup, BranchPattern,
                            Brightworks Sustainability, Buro Happold, BVH Architecture,
                            DCI Engineers, EHDD, Ellenzweig, Gensler, GGLO, Glumac,
                            Group 14 Engineering, Ha/f ClimateDesign, HOK, KieranTimberlake,
                            KPFF Consulting Engineers, Lake|Flato, LMN Architects,
                            Mahlum Architects, Mead & Hunt, Inc., Mithun, Perkins&Will,
                            reLoad Sustainable Design Inc., SERA Architects, Stok,
                            The Green Engineer Inc., The Miller Hull Partnership, LLP.,
                            Walter P Moore, and ZGF Architects LLP.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### Citation
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            Chafart, M., Benke, B., Simonen, K. (2025). WBLCA Benchmark Study v2 Dashboard
                            (Version 1.0) \[Computer Software]. Life Cycle Lab,
                            https://wblca-benchmark-v2.lifecyclelab.org/
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            **[(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0)**
                            2025
                            ''',
                            className='fw-light text-center'
                        ),
                    ],
                    xs=9, sm=9, md=9, lg=9, xl=8, xxl=8,
                    class_name='pe-5'
                ),
                dbc.Col(
                    [
                        typology_jumbotron, project_number_jumbotron, avg_impact_jumbotron
                    ],
                    className='my-4',
                    xs=3, sm=3, md=3, lg=3, xl=2, xxl=2,
                ),
            ],
            justify='center',
            className='m-2'
        ),
    ]
)

# *  **Stacked bar chart** - a way to compare average impacts.
# This chart will show the _average_ impacts of a categorical
# variable split across either life cycle stage or building
# element (as described by OmniClass).
# *  **Parallel coordinates chart** - a way to compare different
# continuous variables and impacts. This chart will show each
# building's categorical values along with their impacts. This will
# allow the user to select different values and see how their building
# will compare against others.
